# -*- coding: utf-8 -*-
"""
Find directories
"""
# Import pop libs
import pop.dicts

# Import python libs
import os
import sys
import importlib
from typing import Any, Dict, Iterable, List


def dir_list(
    subname: str, p_name: str, pypath: List[str] = None, static: List[str] = None
) -> List[str]:
    """
    Return the directories to look for modules in, pypath specifies files
    relative to an installed python package, static is for static dirs
    :param subname: ignored
    :param p_name: ignored
    :param pypath: One or many python paths which will be imported
    :param static: Directories that can be explicitly passed
    """
    ret = []
    for path in pypath:
        mod = importlib.import_module(path)
        for m_path in mod.__path__:
            # If we are inside of an executable the path will be different
            ret.append(m_path)
    ret.extend(static)
    return ret


def inline_dirs(dirs: Iterable[str], subdir: str) -> List[str]:
    """
    Look for the named subdir in the list of dirs
    :param dirs: The names of configured dynamic dirs
    :param subdir: The name of the subdir to check for in the list of dynamic dirs
    :return An extended list of dirs that includes the found subdirs
    """
    ret = []
    for dir_ in dirs:
        check = os.path.join(dir_, subdir)
        if os.path.isdir(check):
            ret.append(check)
    return ret


def dynamic_dirs() -> Dict[str, Any]:
    """
    Iterate over the available python package imports and look for configured
    dynamic dirs
    """
    dirs = []
    ret = {}
    for dir_ in sys.path:
        if not os.path.isdir(dir_):
            continue
        for sub in os.listdir(dir_):
            full = os.path.join(dir_, sub)
            if full.endswith(".egg-link"):
                with open(full) as rfh:
                    dirs.append(rfh.read().strip())
            if os.path.isdir(full):
                dirs.append(full)
    for dir_ in dirs:
        conf = os.path.join(dir_, "conf.py")
        context = {}
        if not os.path.isfile(conf):
            continue
        try:
            with open(conf) as f:
                code = f.read()
                if "DYNE" in code:
                    exec(code, context)
                else:
                    continue
        except Exception:
            continue
        if "DYNE" in context:
            if not isinstance(context["DYNE"], dict):
                continue
            for name, paths in context["DYNE"].items():
                if not isinstance(paths, list):
                    continue
                if name not in ret:
                    ret[name] = {"paths": [], "CONFIG": {}, "CLI_CONFIG": {}}
                if "CONFIG" in context:
                    pop.dicts.update(ret[name]["CONFIG"], context["CONFIG"])
                if "CLI_CONFIG" in context:
                    pop.dicts.update(ret[name]["CLI_CONFIG"], context["CLI_CONFIG"])
                for path in paths:
                    ref = os.path.join(dir_, path.replace(".", os.sep))
                    if dir_.endswith(name):
                        ret[name]["paths"].insert(0, ref)
                    else:
                        ret[name]["paths"].append(ref)
    for name in ret:
        if not ret[name]:
            continue
        first = ret[name]["paths"].pop(0)
        ret[name]["paths"] = sorted(ret[name]["paths"])
        ret[name]["paths"].insert(0, first)
    return ret
