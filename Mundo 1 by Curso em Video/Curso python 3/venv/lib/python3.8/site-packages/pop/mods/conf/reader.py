# -*- coding: utf-8 -*-
"""
The reader module is used to read the config data. This will read in cli
arguments and merge them with config fie arguments.
"""
# Import python libs
import warnings

# Priority order: cli, config, cli_defaults

__virtualname__ = "reader"
__contracts__ = [__virtualname__]


def _merge_dicts(opts, updates, os_opts, explicit_cli_args):
    """
    recursively merge updates into opts
    """
    for key, val in os_opts.items():
        if not val:
            # Don't use empty os vals
            continue
        if key in opts:
            opts[key] = val
    for key, val in updates.items():
        if isinstance(val, dict) and isinstance(opts.get(key), dict):
            _merge_dicts(opts.get(key, {}), val, os_opts, explicit_cli_args)
        elif val is not None:
            if key not in opts:
                # The key is not in opts(from config file), let's add it
                opts[key] = val
                continue

            # We already have a value for the key in opts
            if opts[key] == val:
                # The value is the same, carry on
                continue

            if key in explicit_cli_args:
                # We have a value for the key in opts(from config file) but
                # this option was explicitly passed on the CLI, ie, it's not
                # a default value.
                # Overwrite what's in opts
                opts[key] = val
                continue
    return opts


def read(
    hub,
    defaults,
    subs=None,
    loader="json",
    process_cli=True,
    process_cli_known_args_only=False,
    args=None,
    namespace=None,
):
    """
    Pass in the default options dict to use
    :param opts:
    :param process_cli: Process the passed args or sys.argv
    :param process_cli_known_args_only: Tells the ArgumentParser to only process known arguments
    :param args: Arguments to pass to ArgumentParser
    :param namespace: argparse.Namespace to pass to ArgumentParser
    :return: options
    """
    msg = "Pop-config is the new means to load configs in pop, reader.read will be removed in pop 13"
    warnings.warn(msg, DeprecationWarning, stacklevel=2)
    hub.conf._loader = loader
    if subs:
        hub.conf.args.subs(subs)
    opts = hub.conf.args.setup(defaults)["return"]
    os_opts = hub.conf.os.gather(defaults)
    if process_cli is True:
        cli_opts = hub.conf.args.parse(args, namespace, process_cli_known_args_only)[
            "return"
        ]
    else:
        cli_opts = {}
    explicit_cli_args = cli_opts.pop("_explicit_cli_args_", set())
    cli_opts = hub.conf.args.render(defaults, cli_opts, explicit_cli_args)
    kwargs = {}
    # Due to the order of priorities and the representation of defaults in the
    # Argparser we need to manually check if the config option values are from
    # the cli or from defaults
    f_func = False
    if "config_dir" in cli_opts:
        if cli_opts["config_dir"]:
            kwargs["confdir"] = cli_opts["config_dir"]
        else:
            kwargs["confdir"] = opts["config_dir"]
        if "config_recurse" in cli_opts:
            if cli_opts["config_recurse"]:
                kwargs["recurse"] = cli_opts["config_recurse"]
            else:
                kwargs["recurse"] = opts["config_recurse"]
        # If the config_dir configuration dictionary provides a configuration
        # file pattern to read, pass it along
        kwargs["pattern"] = defaults["config_dir"].get("pattern")
        f_func = hub.conf.file.load_dir
    elif "config" in cli_opts:
        if cli_opts["config"]:
            kwargs["paths"] = cli_opts["config"]
        else:
            kwargs["paths"] = opts["config"]
        f_func = hub.conf.file.load_file
    # Render args before config parsing
    if f_func:
        f_opts = f_func(**kwargs)
        opts.update(f_opts)
        return _merge_dicts(opts, cli_opts, os_opts, explicit_cli_args)
    else:
        return _merge_dicts(opts, cli_opts, os_opts, explicit_cli_args)
