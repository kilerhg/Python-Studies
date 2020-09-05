# -*- coding: utf-8 -*-
"""
Configuration file core loading functions
"""

# Import python libs
import os
import glob
import fnmatch


def parse(hub, raw, cli, os_vars, cli_args, loader):
    """
    Determine if a config file or a config dir has been set up and load it up!
    """
    # This function is the entry point for the config.file sub
    # Figure out what config file value to use in this priority
    default = raw[cli]["CONFIG"].get("config", {}).get("default")
    default_dir = raw[cli]["CONFIG"].get("config_dir", {}).get("default")
    os_conf = os_vars.get("config", default)
    os_dir = os_vars.get("config_dir", default_dir)
    conf = cli_args.get("config", os_conf)
    dir_ = cli_args.get("config_dir", os_dir)
    file_opts = {}
    dir_opts = {}
    if dir_:
        file_opts = hub.config.file.init.load_dir(dir_, loader)
    if conf:
        dir_opts = hub.config.file.init.load(conf, loader)
    ret = hub.pop.dicts.update(dir_opts, file_opts)
    return ret


def load(hub, paths, loader, includes=True):
    """
    Load a single configuration file
    """
    opts = {}
    if not isinstance(paths, list):
        paths = [paths]
    add = []
    for fn in paths:
        add.extend(glob.glob(fn))
    paths.extend(add)
    for fn in paths:
        fn_data = hub.config.render.init.load_file(loader, fn)
        if includes:
            fn_data = hub.config.file.init.proc_include(fn, fn_data, loader)
        hub.pop.dicts.update(opts, fn_data)
    return opts


def load_dir(
    hub, confdir, loader, includes=True, recurse=True,
):
    """
    Load takes a directory location to scan for configuration files. These
    files will be read in.
    """
    opts = {}
    if not isinstance(confdir, list):
        confdir = [confdir]
    confdirs = []
    for dirs in confdir:
        if not isinstance(dirs, (list, tuple)):
            dirs = [dirs]
        for dir_ in dirs:
            confdirs.extend(glob.glob(dir_))
    paths = []
    for dir_ in confdirs:
        dirpaths = []
        if os.path.isdir(dir_):
            if not recurse:
                for fn_ in os.listdir(dir_):
                    path = os.path.join(dir_, fn_)
                    if os.path.isdir(path):
                        # Don't process directories
                        continue
                    dirpaths.append(path)
            else:
                for root, dirs, files in os.walk(dir_):
                    for fn_ in files:
                        path = os.path.join(root, fn_)
                        dirpaths.append(path)

        # Sort confdir directory paths like:
        # /b.txt
        # /c.txt
        # /a/x.txt
        # /b/x.txt
        paths.extend(sorted(dirpaths, key=lambda p: (p.count(os.path.sep), p)))
    opts = hub.pop.dicts.update(
        opts, hub.config.file.init.load(paths, loader, includes)
    )
    return opts


def proc_include(hub, fn, opts, loader):
    """
    Process include and include_dir
    """
    dirname = os.path.dirname(fn)
    if opts.get("include_dir"):
        idir = opts.pop("include_dir")
        if not idir.startswith(os.path.abspath(os.sep)):
            idir = os.path.join(dirname, idir)
        opts = hub.pop.dicts.update(opts, hub.config.file.init.load_dir(idir, loader))
        hub.config.file.init.proc_include(os.path.join(idir, "f"), opts, loader)
    if opts.get("include"):
        ifn = opts.pop("include")
        if not ifn.startswith(os.path.abspath(os.sep)):
            ifn = os.path.join(dirname, ifn)
        opts = hub.pop.dicts.update(opts, hub.config.file.init.load(ifn, loader))
        hub.config.file.init.proc_include(ifn, opts, loader)
    return opts
