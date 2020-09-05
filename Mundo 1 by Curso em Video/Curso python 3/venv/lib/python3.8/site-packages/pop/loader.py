# -*- coding: utf-8 -*-
"""
Load the files detected from the scanner
"""
# Import Python libs
import asyncio
import os
import sys
import inspect
import importlib
import importlib.util
import importlib.machinery
import traceback as stdlib_traceback
import types
from typing import Any, Dict, List, Tuple

# Import pop libs
import pop.exc
import pop.contract


class LoadError(Exception):
    """
    Errors from the loader are contained herein
    """

    __slots__ = ("edict", "traceback")

    def __init__(self, msg, exception=None, traceback=None, verror=None):
        self.edict = {
            "msg": msg,
            "exception": exception,
            "verror": verror,
        }
        self.traceback = traceback

    def __call__(self):
        """
        Return the error cases
        """
        return self.edict

    def __getattr__(self, attr):
        """
        Return a lambda that returns the edict
        """
        return self.__calling_load_error__

    def __calling_load_error__(
        self, *args, **kwargs
    ):  # pylint: disable=unused-argument
        if self.edict["verror"]:
            error = "{0[msg]}: {0[verror]}".format(self())
            raise pop.exc.PopError(error)
        error = "{0[msg]}: {0[exception]!r}".format(self())
        if self.traceback:
            error += "\n" + self.traceback
        raise pop.exc.PopError(error)

    def __repr__(self):
        return "<{} edict={!r}>".format(self.__class__.__name__, self.edict)


def load_mod(modname: str, form: str, path: str) -> "LoadedMod":
    """
    Load a single module
    :param form: The name of the loader module
    :param modname: The name of the module to get from the loader
    :param path: The package to use as the anchor point from which to resolve the
        relative import to an absolute import.
    """
    this = sys.modules[__name__]
    return getattr(this, form)(modname, path)


def _generate_module(name: str) -> types.ModuleType:
    """
    Generate a module at runtime and insert it in sys.modules
    :param name: The name of the module to create
    """
    if name in sys.modules:
        return sys.modules[name]

    code = "'''POP sub auto generated parent module for {0}'''".format(
        name.split(".")[-1]
    )
    # Create a new module that is not entered into sys.modules
    module = types.ModuleType(name)
    exec(code, module.__dict__)  # pylint: disable=exec-used
    sys.modules[name] = module
    return module


def _populate_sys_modules(mod: "LoadedMod"):
    """
    This is a hack to populate sys.modules with the modules that pop loads
    while making sure that parent modules have the attribute for the child
    modules.
    """
    mod_parts = mod.split(".")
    imp_mod = mod_parts.pop(0)
    gen_mod = _generate_module(imp_mod)
    while True:
        if not mod_parts:
            break
        part = mod_parts.pop(0)
        imp_mod += "." + part
        gen_child_mod = _generate_module(imp_mod)
        setattr(gen_mod, part, gen_child_mod)
        gen_mod = gen_child_mod


def ext(modname: str, path: str) -> "LoadedMod" or LoadError:
    """
    Attempt to load the named python modules
    :param modname: The name of the module to get from the loader
    :param path: The package to use as the anchor point from which to resolve the
        relative import to an absolute import.
    """
    modname = ".".join(modname.split(".")[:-1])
    if modname in sys.modules:
        return sys.modules[modname]
    _populate_sys_modules(modname)
    try:
        efl = importlib.machinery.ExtensionFileLoader(modname, path)
        mod = efl.create_module(importlib.util.find_spec(modname))
        return efl.exec_module(mod)
    except Exception as exc:  # pylint: disable=broad-except
        return LoadError(
            "Failed to load python module {} at path {}".format(modname, path),
            exception=exc,
            traceback=stdlib_traceback.format_exc(),
        )


def python(modname: str, path: str) -> "LoadedMod" or LoadError:
    """
    Attempt to load the named python modules
    :param modname: The name of the module to get from the loader
    :param path: The package to use as the anchor point from which to resolve the
        relative import to an absolute import.
    """
    if modname in sys.modules:
        return sys.modules[modname]
    try:
        sfl = importlib.machinery.SourceFileLoader(modname, path)
        return sfl.load_module()
    except Exception as exc:  # pylint: disable=broad-except
        return LoadError(
            "Failed to load python module {} at path {}".format(modname, path),
            exception=exc,
            traceback=stdlib_traceback.format_exc(),
        )


def _base_name(bname: str, mod: "LoadedMod") -> Tuple[str, str]:
    """
    Find the basename and alias of a loader module
    :param bname: The base name of the mod's path
    :param mod: A loader module or a LoadError if the module didn't load
    """
    base_name = os.path.basename(bname)
    if "." in base_name:
        base_name = base_name.split(".")[0]
    return base_name, getattr(mod, "__virtualname__", base_name)


def _load_virtual(
    hub: "pop.hub.Hub",
    virtual: bool,
    mod: "LoadedMod" or LoadError,
    bname: str,
    vtype: str,
) -> Dict[str, Any]:
    """
    Run the virtual function to name the module and check for all loader
    errors
    :param hub: The redistributed pop central hub
    :param virtual: Toggle whether or not to process __virtual__ functions
    :param mod: A loader module or a LoadError if the module didn't load
    :param bname: The base name of the mod's path
    :param vtype: The name of the virtual function to call on the module I.E. __virtual__ or __sub_virtual__
    """
    base_name, name = _base_name(bname, mod)

    if isinstance(mod, LoadError):
        # The mod is a LoadError instance.
        # Return the load error with name as the base_name because another
        # module is still allowed to load under the same __virtualname__
        # but also return the vname information
        return {"name": base_name, "vname": name, "error": mod}

    if not virtual:
        # __virtual__ is not to be processed. Return now!
        return {"name": base_name}

    if not hasattr(mod, vtype):
        # No __virtual__ processing is required.
        # Return the mod's name as the defined __virtualname__ if defined,
        # else, the base_name
        return {"name": name}

    try:
        vret = getattr(mod, vtype)(hub)
        # If the __virtual__ function was asynchronous then run it in an asyncio loop
        if asyncio.iscoroutine(vret):
            vret = asyncio.get_running_loop().run_until_complete(vret)
    except Exception as exc:  # pylint: disable=broad-except
        err = LoadError(
            "Virtual threw exception in mod {}".format(bname),
            exception=exc,
            traceback=stdlib_traceback.format_exc(),
        )
        # Return the load error with name as the base_name because another
        # module is still allowed to load under the same __virtualname__
        # but also return the vname information
        return {"name": base_name, "vname": name, "error": err}

    verror = vret
    if isinstance(vret, tuple):
        if len(vret) > 1:
            verror = vret[1]
        vret = vret[0]

    if vret is True:
        # No problems occurred, module is allowed to load
        # Return the mod's name as the defined __virtualname__ if defined,
        # else, the base_name
        return {"name": name}

    if vret is False:
        # __virtual__ explicitly disabled the loading of this module
        err = LoadError("Module {} returned virtual FALSE".format(bname), verror=verror)
        # Return the load error with name as the base_name because another
        # module is still allowed to load under the same __virtualname__
        # but also return the vname information
        return {"name": base_name, "vname": name, "error": err}

    # Anything else besides True/False should be considered a LoadError
    err = LoadError("Module {} returned virtual error".format(bname), verror=verror)
    # Return the load error with name as the base_name because another
    # module is still allowed to load under the same __virtualname__
    # but also return the vname information
    return {"name": base_name, "vname": name, "error": err}


def load_virtual(
    hub: "pop.hub.Hub", virtual: bool, mod: "LoadedMod" or LoadError, bname: str
) -> Dict[str, Any]:
    """
    Run the __virtual__ function to name the module and check for all loader errors
    :param hub: The redistributed pop central hub
    :param virtual: Toggle whether or not to process __virtual__ functions
    :param mod: A loader module or a LoadError if the module didn't load
    :param bname: The base name of the mod's path
    """
    return _load_virtual(hub, virtual, mod, bname, "__virtual__")


def load_sub_virtual(
    hub: "pop.hub.Hub", virtual: bool, mod: "LoadedMod" or LoadError, bname: str
) -> Dict[str, Any]:
    """
    Run the __sub_virtual__ function to name the module and check for all loader errors
    :param hub: The redistributed pop central hub
    :param virtual: Toggle whether or not to process __virtual__ functions
    :param mod: A loader module or a LoadError if the module didn't load
    :param bname: The base name of the mod's path
    """
    _, name = _base_name(bname, mod)
    if name != "init":
        return {"name": name}
    return _load_virtual(hub, virtual, mod, bname, "__sub_virtual__")


def mod_init(sub: "pop.hub.Sub", mod: "LoadedMod", mod_name: str):
    """
    Process module's __init__ function if defined
    :param sub: The pop object that contains the loaded module data
    :param mod: A loader modul
    :param mod_name: The name of the module to get from the loader
    """
    if "__init__" in dir(mod):
        init = pop.contract.Contracted(
            sub._hub,
            contracts=[],
            func=mod.__init__,
            ref=f"{sub._subname}.{mod_name}",
            name="__init__",
        )
        ret = init()
        # If the __init__ function was asynchronous then run it in an asyncio loop
        if asyncio.iscoroutine(ret):
            asyncio.get_running_loop().run_until_complete(ret)


def sub_alias(this_sub: "pop.hub.Sub", mod: "LoadedMod", mod_name: str):
    """
    Check the sub alias settings and apply the alias names locally so they can be gathered into the higher level object on the hub
    :param this_sub: The pop object that contains the loaded module data
    :param mod: A loader module
    :param mod_name: The name of the module to get from the loader
    """
    if mod_name == "init":
        alias = getattr(mod, "__sub_alias__", [])
        if alias:
            this_sub._alias = alias


def prep_loaded_mod(
    this_sub: "pop.hub.Sub",
    mod: "LoadedMod",
    mod_name: str,
    contracts: List[pop.contract.Wrapper],
) -> "LoadedMod":
    """
    Read the attributes of a python module and create a LoadedMod, which resolves
    aliases and omits objects that should not be exposed.
    :param this_sub: The pop object that contains the loaded module data
    :param mod: A loader module
    :param mod_name: The name of the module to get from the loader
    :param contracts: Contracts functions to add to the sub
    """
    lmod = this_sub._loaded.get(mod_name, LoadedMod(mod_name))
    ref = f"{this_sub._subname}.{mod_name}"  # getattr(hub, ref) should resolve to this module
    sub_alias(this_sub, mod, mod_name)
    for attr in getattr(mod, "__load__", dir(mod)):
        name = getattr(mod, "__func_alias__", {}).get(attr, attr)
        func = getattr(mod, attr)
        if not this_sub._omit_vars:
            if (
                not inspect.isfunction(func)
                and not inspect.isclass(func)
                and type(func).__name__ != "cython_function_or_method"
            ):
                lmod._vars[name] = func
                lmod._attrs[name] = func
                continue
        if attr.startswith(this_sub._omit_start):
            continue
        if attr.endswith(this_sub._omit_end):
            continue
        if (
            inspect.isfunction(func)
            or inspect.isbuiltin(func)
            or type(func).__name__ == "cython_function_or_method"
        ):
            obj = pop.contract.create_contracted(
                this_sub._hub, contracts, func, ref, name
            )
            if not this_sub._omit_func:
                if this_sub._pypath and not func.__module__.startswith(mod.__name__):
                    # We're only interested in functions defined in this module, not
                    # imported functions
                    continue
                lmod._funcs[name] = obj
                lmod._attrs[name] = obj
        else:
            klass = func
            if not this_sub._omit_class and inspect.isclass(klass):
                # We're only interested in classes defined in this module, not
                # imported classes
                if not klass.__module__.startswith(mod.__name__):
                    continue
                lmod._classes[name] = klass
                lmod._attrs[name] = klass
    return lmod


class LoadedMod(types.ModuleType):
    """
    The LoadedMod class allows for the module loaded onto the sub to return
    custom sequencing, for instance it can be iterated over to return all
    functions
    """

    def __init__(self, name: str):
        super().__init__(name)
        self._vars = {}
        self._funcs = {}
        self._classes = {}
        self._attrs = {}

    def __getattr__(self, item: str):
        if item in self._attrs:
            return self._attrs[item]
        raise AttributeError(item)

    def __iter__(self):
        keys = sorted(self._funcs)
        ret = []
        for key in keys:
            ret.append(self._funcs[key])
        return iter(ret)

    def __dir__(self):
        # TODO: This should return finite set attrs as well as dunder attrs
        ret = list(self._attrs.keys())
        ret.extend(["__name__", "_vars", "_funcs", "_classes", "_attrs"])
        return ret
