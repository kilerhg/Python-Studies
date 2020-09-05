# -*- coding: utf-8 -*-
"""
Used to scan the given directories for loadable files
"""
# Import python libs
import os
import importlib.machinery
import collections
from typing import Any, Dict, Iterable

PY_END = (".py", ".pyc", ".pyo")
PYEXT_END = tuple(importlib.machinery.EXTENSION_SUFFIXES)
CYTHON_END = (".pyx",)
SKIP_DIRNAMES = ("__pycache__",)


def scan(dirs: Iterable[str]) -> Dict[str, Dict[str, Any]]:
    """
    :param dirs: A list of locations to search for importables files
    :return A description of importable files
    """
    ret = collections.OrderedDict()
    ret["python"] = collections.OrderedDict()
    ret["cython"] = collections.OrderedDict()
    ret["ext"] = collections.OrderedDict()
    ret["imp"] = collections.OrderedDict()
    for dir_ in dirs:
        for fn_ in os.listdir(dir_):
            _apply_scan(ret, dir_, fn_)
    return ret


def _apply_scan(
    ret: Dict[str, Dict[str, Any]], dir_: str, fn_: str
) -> None or Dict[str, Dict[str, Any]]:
    """
    Convert the scan data into paths and refs
    :param ret: The result of a scan()
    :param dir_:
    :param fn_:
    """
    if fn_.startswith("_"):
        return
    if os.path.basename(dir_) in SKIP_DIRNAMES:
        return
    full = os.path.join(dir_, fn_)
    if "." not in full:
        return
    bname = full[: full.rindex(".")]
    if fn_.endswith(PY_END):
        if bname not in ret["python"]:
            ret["python"][bname] = {"path": full}
    if fn_.endswith(CYTHON_END):
        if bname not in ret["cython"]:
            ret["cython"][bname] = {"path": full}
    if fn_.endswith(PYEXT_END):
        if bname not in ret["ext"]:
            ret["ext"][bname] = {"path": full}
