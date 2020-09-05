# -*- coding: utf-8 -*-
"""
Tools to work with dicts
"""
import dict_tools.update
import dict_tools.data
import warnings

__virtualname__ = "dicts"


def update(*args, **kwargs):
    warnings.warn("Use `dict_tools.update.update()` instead", DeprecationWarning)
    return dict_tools.update.update(*args, **kwargs)


def traverse(*args, **kwargs):
    warnings.warn(
        "Use `dict_tools.data.traverse_dict_and_list()` instead", DeprecationWarning
    )
    return dict_tools.data.traverse_dict_and_list(*args, **kwargs)
