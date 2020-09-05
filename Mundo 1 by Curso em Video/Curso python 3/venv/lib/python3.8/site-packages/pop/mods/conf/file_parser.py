# -*- coding: utf-8 -*-
"""
Configuration file core loading functions
"""

# Import python libs
import os
import glob
import fnmatch
import pop.hub

__virtualname__ = "file"
__contracts__ = [__virtualname__]


def load_file(hub: "pop.hub.Hub", paths, defaults=None, overrides=None, includes=True):
    """
    Load a single configuration file
    """
    opts = {}
    if isinstance(defaults, dict):
        opts.update(defaults)
    if not isinstance(paths, list):
        paths = paths.split(",")
    add = []
    for fn_ in paths:
        add.extend(glob.glob(fn_))
    paths.extend(add)
    for fn_ in paths:
        if hub.conf._loader == "yaml":
            opts.update(hub.conf.yaml.load(fn_))
        elif hub.conf._loader == "json":
            opts.update(hub.conf.json.load(fn_))
        elif hub.conf._loader == "toml":
            opts.update(hub.conf.toml.load(fn_))
    if includes:
        hub.conf.file.proc_include(opts)
    if isinstance(overrides, dict):
        opts.update(overrides)
    return opts


def load_dir(
    hub,
    confdir,
    defaults=None,
    overrides=None,
    includes=True,
    recurse=False,
    pattern=None,
):
    """
    Load takes a directory location to scan for configuration files. These
    files will be read in. The defaults dict defines what
    configuration options should exist if not found in the confdir. Overrides
    are configuration options which should be included regardless of whether
    those options existed before. If includes is set to True, then the
    statements 'include' and 'include_dir' found in either the defaults or
    in configuration files.
    """
    opts = {}
    if not isinstance(confdir, list):
        confdir = confdir.split(",")
    confdirs = []
    for dirs in confdir:
        if not isinstance(dirs, (list, tuple)):
            dirs = [dirs]
        for dir_ in dirs:
            confdirs.extend(glob.glob(dir_))
    if isinstance(defaults, dict):
        opts.update(defaults)
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
                    if pattern and not fnmatch.fnmatch(fn_, pattern):
                        continue
                    dirpaths.append(path)
            else:
                for root, dirs, files in os.walk(dir_):
                    for fn_ in files:
                        path = os.path.join(root, fn_)
                        if pattern and not fnmatch.fnmatch(fn_, pattern):
                            continue
                        dirpaths.append(path)

        # Sort confdir directory paths like:
        # /b.txt
        # /c.txt
        # /a/x.txt
        # /b/x.txt
        paths.extend(sorted(dirpaths, key=lambda p: (p.count(os.path.sep), p)))
    opts.update(hub.conf.file.load_file(paths, includes))
    if isinstance(overrides, dict):
        opts.update(overrides)
    return opts


def proc_include(hub: "pop.hub.Hub", opts):
    """
    process include and include_dir
    """
    rec = False
    if opts.get("include_dir"):
        idir = opts.pop("include_dir")
        opts.update(hub.conf.file.load_dir(idir))
        rec = True
    if opts.get("include"):
        ifn = opts.pop("include")
        opts.update(hub.conf.file.load_file(ifn))
        rec = True
    if rec:
        hub.conf.file.proc_include(opts)
    return opts
