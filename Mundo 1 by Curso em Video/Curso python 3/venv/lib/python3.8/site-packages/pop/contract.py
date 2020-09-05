# -*- coding: utf-8 -*-
"""
Contracts to enforce loader objects
"""

# Import python libs
import asyncio
import functools
import inspect
import os
from collections import namedtuple
from types import ModuleType
from typing import Dict, Iterable, List

# Import pop libs
import pop.exc
import pop.hub
import pop.verify


class ContractedContext(
    namedtuple(
        "ContractedContext",
        ("func", "args", "kwargs", "signature", "ret", "cache", "ref"),
    )
):
    """
    Contracted function calling context
    """

    def __new__(
        cls,
        func: functools.partial,
        args: Iterable,
        kwargs: Dict,
        signature,
        ref,
        ret=None,
        cache=None,
    ):  # pylint: disable=too-many-arguments
        if cache is None:
            cache = {}
        return super(ContractedContext, cls).__new__(
            cls, func, list(args), kwargs, signature, ret, cache, ref
        )

    def get_argument(self, name):
        """
        Return the value corresponding to a function argument after binding the contract context
        argument and keyword arguments to the function signature.
        """
        return self.get_arguments()[name]

    def get_arguments(self):
        """
        Return a dictionary of all arguments that will be passed to the function and their
        values, including default arguments.
        """
        if "__bound_signature__" not in self.cache:
            try:
                self.cache["__bound_signature__"] = self.signature.bind(
                    *self.args, **self.kwargs
                )
            except TypeError as e:
                for frame in inspect.trace(0):
                    if frame.function == "bind" and frame.filename.endswith(
                        os.sep + "inspect.py"
                    ):
                        raise pop.exc.BindError(e)
                raise
            # Apply any default values from the signature
            self.cache["__bound_signature__"].apply_defaults()
        return self.cache["__bound_signature__"].arguments


def load_contract(
    contracts: List["Contracted"],
    default_contracts: List[str],
    mod: ModuleType,
    name: str,
) -> List:
    """
    return a Contract object loaded up
    Dynamically create the correct Contracted type
    :param contracts: Contracts functions to add to the sub
    :param default_contracts: The contracts that have been marked as defaults
    :param mod: A loader module
    :param name: The name of the module to get from the loader
    """
    raws = []
    if not contracts:
        return raws
    loaded_contracts = []
    if hasattr(contracts, name):
        loaded_contracts.append(name)
        raws.append(getattr(contracts, name))
    if hasattr(contracts, "init"):
        loaded_contracts.append("init")
        raws.append(getattr(contracts, "init"))
    if default_contracts:
        for contract in default_contracts:
            if contract in loaded_contracts:
                continue
            loaded_contracts.append(contract)
            raws.append(getattr(contracts, contract))
    if hasattr(mod, "__contracts__"):
        cnames = getattr(mod, "__contracts__")
        if not isinstance(cnames, (list, tuple)):
            cnames = cnames.split(",")
        for cname in cnames:
            if cname in contracts:
                if cname in loaded_contracts:
                    continue
                loaded_contracts.append(cname)
                raws.append(getattr(contracts, cname))
    return raws


class Wrapper:
    def __init__(self, func: functools.partial, ref: str, name: str):
        """
        :param func: The contracted function to call
        :param ref: The reference to the function on the hub
        :param name: An alias for the function
        """
        self.__dict__.update(
            getattr(func, "__dict__", {})
        )  # do this first so we later overwrite any conflicts
        self.func = func
        self.ref = ref
        self.__name__ = name
        self.signature = inspect.signature(self.func)
        self._sig_errors = []
        self.__wrapped__ = func

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)

    def __repr__(self):
        return "<{} func={}.{}>".format(
            self.__class__.__name__, self.func.__module__, self.__name__
        )


class Contracted(Wrapper):
    """
    This class wraps functions that have a contract associated with them
    and executes the contract routines
    """

    def __init__(
        self,
        hub: "pop.hub.Hub",
        contracts: List[Wrapper],
        func: functools.partial,
        ref: str,
        name: str,
    ):
        super().__init__(func, ref, name)
        self.hub = hub
        self.contracts = contracts or []
        self._load_contracts()

    def _get_contracts_by_type(self, contract_type: str = "pre") -> List[Wrapper]:
        """
        :param contract_type: One of "call", "pre", "post", or "sig"
        """
        matches = []
        fn_contract_name = "{}_{}".format(contract_type, self.__name__)
        for contract in self.contracts:
            if hasattr(contract, fn_contract_name):
                matches.append(getattr(contract, fn_contract_name))
            if hasattr(contract, contract_type):
                matches.append(getattr(contract, contract_type))

        return matches

    def _load_contracts(self):
        # TODO:
        # if Contracted - only allow regular pre/post
        # if ContractedAsync - allow coroutines and functions
        # if ContractedAsyncGen - allow coroutines and functions

        self.contract_functions = {
            "pre": self._get_contracts_by_type("pre"),
            "call": self._get_contracts_by_type("call")[:1],
            "post": self._get_contracts_by_type("post"),
        }
        # TODO: write test for stack-like behavior (reverse "pre")
        self._has_contracts = (
            sum([len(l) for l in self.contract_functions.values()]) > 0
        )

    def __call__(self, *args, **kwargs):
        args = (self.hub,) + args
        if not self._has_contracts:
            return self.func(*args, **kwargs)
        contract_context = ContractedContext(
            self.func, args, kwargs, self.signature, self.ref
        )

        for fn in self.contract_functions["pre"]:
            fn(contract_context)
        if self.contract_functions["call"]:
            ret = self.contract_functions["call"][0](contract_context)
        else:
            ret = self.func(*contract_context.args, **contract_context.kwargs)
        for fn in self.contract_functions["post"]:
            post_ret = fn(contract_context._replace(ret=ret))
            if post_ret is not None:
                ret = post_ret

        return ret


class ContractedAsyncGen(Contracted):
    async def __call__(self, *args, **kwargs):
        args = (self.hub,) + args
        if not self._has_contracts:
            async for chunk in self.func(*args, **kwargs):
                yield chunk
            return
        contract_context = ContractedContext(
            self.func, args, kwargs, self.signature, self.ref
        )

        for fn in self.contract_functions["pre"]:
            pre_ret = fn(contract_context)
            if asyncio.iscoroutine(pre_ret):
                await pre_ret
        chunk = None
        if self.contract_functions["call"]:
            async for chunk in self.contract_functions["call"][0](contract_context):
                yield chunk
        else:
            async for chunk in self.func(
                *contract_context.args, **contract_context.kwargs
            ):
                yield chunk
        ret = chunk
        for fn in self.contract_functions["post"]:
            if isinstance(fn, ContractedAsync):
                post_ret = await fn(contract_context._replace(ret=ret))
            else:
                post_ret = fn(contract_context._replace(ret=ret))
            if post_ret is not None:
                ret = post_ret


class ContractedAsync(Contracted):
    async def __call__(self, *args, **kwargs):
        args = (self.hub,) + args
        if not self._has_contracts:
            return await self.func(*args, **kwargs)
        contract_context = ContractedContext(
            self.func, args, kwargs, self.signature, self.ref
        )

        for fn in self.contract_functions["pre"]:
            pre_ret = fn(contract_context)
            if asyncio.iscoroutine(pre_ret):
                await pre_ret
        if self.contract_functions["call"]:
            ret = await self.contract_functions["call"][0](contract_context)
        else:
            ret = await self.func(*contract_context.args, **contract_context.kwargs)
        for fn in self.contract_functions["post"]:
            if isinstance(fn, ContractedAsync):
                post_ret = await fn(contract_context._replace(ret=ret))
            else:
                post_ret = fn(contract_context._replace(ret=ret))
            if post_ret is not None:
                ret = post_ret

        return ret


def create_contracted(
    hub: "pop.hub.Hub",
    contracts: List[Wrapper],
    func: functools.partial,
    ref: str,
    name: str,
) -> Contracted:
    """
    Dynamically create the correct Contracted type
    :param hub: The redistributed pop central hub
    :param contracts: Contracts functions to add to the sub
    :param func: The contracted function to call
    :param ref: The reference to the function on the hub
    :param name: The name of the module to get from the loader
    """
    if asyncio.iscoroutinefunction(func):
        return ContractedAsync(hub, contracts, func, ref, name)
    elif inspect.isasyncgenfunction(func):
        return ContractedAsyncGen(hub, contracts, func, ref, name)
    else:
        return Contracted(hub, contracts, func, ref, name)
