# -*- coding: utf-8 -*-
"""
Translate an options data structure into command line args
"""

# Import python libs
import sys
import inspect
import argparse
import functools
import collections
import pop.hub

__virtualname__ = "args"
__contracts__ = [__virtualname__]


class ActionWrapper:
    """
    This class wraps argparse.Action instances in order to mark arguments passed
    on CLI as explicitly passed
    """

    def __init__(self, action):
        self._action = action
        functools.update_wrapper(self, action)

    def __call__(self, parser, namespace, values, option_string):
        # Let's store the call to this option as an explicit CLI call for later
        # use when overwriting any configuration settings on file with those
        # from CLI
        if getattr(parser, "_explicit_cli_args_", None) is None:
            setattr(parser, "_explicit_cli_args_", set())
        parser._explicit_cli_args_.add(
            self._action.dest
        )  # pylint: disable=protected-access
        # Carry on regular operation
        return self._action(parser, namespace, values, option_string)

    def __getattribute__(self, name):
        if name == "_action":
            return object.__getattribute__(self, name)
        # Proxy any attribute's search to the _action instance
        return getattr(self._action, name)

    def __repr__(self):
        return repr(self._action)


class ActionClassWrapper:
    """
    This class wraps argparse.Action classes in order to mark arguments passed
    on CLI as explicitly passed
    """

    def __init__(self, klass):
        self._klass = klass

    def __call__(self, *args, **kwargs):
        return ActionWrapper(self._klass(*args, **kwargs))

    def __repr__(self):
        return repr(self._klass)

    def __getattribute__(self, name):
        if name == "_klass":
            return object.__getattribute__(self, name)
        # Proxy any attributes search to the _klass instance
        return getattr(self._klass, name)


class ArgumentParser(argparse.ArgumentParser):
    def register(self, name, value, obj):  # pylint: disable=arguments-differ
        if name == "action":
            # Let's wrap it on our action class wrapper so we can latter store
            # which options were explicitly passed from CLI
            return super(ArgumentParser, self).register(
                name, value, ActionClassWrapper(obj)
            )
        return super(ArgumentParser, self).register(name, value, obj)

    def parse_known_args(self, args=None, namespace=None):
        namespace, arg_strings = super().parse_known_args(args, namespace)
        explicit_cli_args = getattr(self, "_explicit_cli_args_", set())
        if "_explicit_cli_args_" not in namespace:
            setattr(namespace, "_explicit_cli_args_", set())
        namespace._explicit_cli_args_.update(explicit_cli_args)
        return namespace, arg_strings


def __init__(hub: "pop.hub.Hub"):
    """
    Set up the local memory copy of the parser
    """
    hub.conf._mem["args"] = {}


def _init_parser(hub: "pop.hub.Hub", opts):
    if "parser" not in hub.conf._mem["args"]:
        # Instantiate the parser
        hub.conf._mem["args"]["parser"] = ArgumentParser(**opts.get("_argparser_", {}))


def _keys(opts):
    """
    Return the keys in the right order
    """
    if isinstance(opts, collections.OrderedDict):
        return sorted(
            list(opts), key=lambda k: opts[k].get("display_priority", sys.maxsize)
        )
    return sorted(opts, key=lambda k: (opts[k].get("display_priority", sys.maxsize), k))


def subs(hub: "pop.hub.Hub", opts):
    """
    Set up sub parsers, if using sub parsers this needs to be called
    before calling setup.

    opts dict:
        <sub_title>:
            [desc]: 'Some subparser'
            help: 'subparser!'
    """
    _init_parser(hub, opts)
    hub.conf._mem["args"]["sub"] = hub.conf._mem["args"]["parser"].add_subparsers(
        dest="_subparser_"
    )
    hub.conf._mem["args"]["subs"] = {}
    for arg in _keys(opts):
        if arg in ("_argparser_",):
            continue
        comps = opts[arg]
        kwargs = {}
        if "help" in comps:
            kwargs["help"] = comps["help"]
        if "desc" in comps:
            kwargs["description"] = comps["desc"]
        hub.conf._mem["args"]["subs"][arg] = hub.conf._mem["args"]["sub"].add_parser(
            arg, **kwargs
        )
    return {"result": True, "return": True}


def setup(hub: "pop.hub.Hub", opts):
    """
    Take in a pre-defined opts dict and translate it to args

    opts dict:
        <arg>:
            [group]: foo
            [default]: bar
            [action]: store_true
            [options]: # arg will be turned into --arg
              - '-A'
              - '--cheese'
            [choices]:
              - foo
              - bar
              - baz
            [nargs]: +
            [type]: int
            [dest]: cheese
            help: Some great help message
    """
    _init_parser(hub, opts)
    defaults = {}
    groups = {}
    ex_groups = {}
    for arg in _keys(opts):
        if arg in ("_argparser_",):
            continue
        comps = opts[arg]
        positional = comps.pop("positional", False)
        if positional:
            args = [arg]
        else:
            long_opts = ["--{}".format(arg.replace("_", "-"))]
            short_opts = []
            for o_str in comps.get("options", []):
                if not o_str.startswith("--") and o_str.startswith("-"):
                    short_opts.append(o_str)
                    continue
                long_opts.append(o_str)
            args = short_opts + long_opts
        kwargs = {}
        kwargs["action"] = action = comps.get("action", None)

        if action is None:
            # Non existing option defaults to a StoreAction in argparse
            action = hub.conf._mem["args"]["parser"]._registry_get(
                "action", action
            )  # pylint: disable=protected-access

        if isinstance(action, str):
            signature = inspect.signature(
                hub.conf._mem["args"]["parser"]._registry_get("action", action).__init__
            )  # pylint: disable=protected-access
        else:
            signature = inspect.signature(action.__init__)

        for param in signature.parameters:
            if param == "self" or param not in comps:
                continue
            if param == "dest":
                kwargs["dest"] = comps.get("dest", arg)
                continue
            if param == "help":
                kwargs["help"] = comps.get("help", "THIS NEEDS SOME DOCUMENTATION!!")
                continue
            if param == "default":
                defaults[comps.get("dest", arg)] = comps[param]
            kwargs[param] = comps[param]

        if "group" in comps:
            group = comps["group"]
            if group not in groups:
                groups[group] = hub.conf._mem["args"]["parser"].add_argument_group(
                    group
                )
            groups[group].add_argument(*args, **kwargs)
            continue
        if "ex_group" in comps:
            group = comps["ex_group"]
            if group not in ex_groups:
                ex_groups[group] = hub.conf._mem["args"][
                    "parser"
                ].add_mutually_exclusive_group()
            ex_groups[group].add_argument(*args, **kwargs)
            continue
        if "sub" in comps:
            subs = comps["sub"]
            if not isinstance(subs, list):
                subs = [subs]
            for sub in subs:
                sparse = hub.conf._mem["args"]["subs"].get(sub)
                if not sparse:
                    # Maybe raise exception here? Malformed config?
                    continue
                sparse.add_argument(*args, **kwargs)
            continue
        hub.conf._mem["args"]["parser"].add_argument(*args, **kwargs)
    return {"result": True, "return": defaults}


def parse(
    hub: "pop.hub.Hub", args=None, namespace=None, only_parse_known_arguments=False
):
    """
    Parse the command line options
    """
    if only_parse_known_arguments:
        opts, unknown_args = hub.conf._mem["args"]["parser"].parse_known_args(
            args, namespace
        )
        opts_dict = opts.__dict__
        opts_dict["_unknown_args_"] = unknown_args
    else:
        opts = hub.conf._mem["args"]["parser"].parse_args(args, namespace)
        opts_dict = opts.__dict__
    return {"result": True, "return": opts_dict}


def render(hub: "pop.hub.Hub", defaults, cli_opts, explicit_cli_args):
    """
    For options specified as such, take the string passed into the cli and
    render it using the specified render flag
    """
    for key in explicit_cli_args:
        rend = defaults.get(key, {}).get("render")
        if rend:
            ref = f"conf.{rend}.render"
            cli_opts[key] = hub.pop.ref.last(ref)(cli_opts[key])
    return cli_opts
