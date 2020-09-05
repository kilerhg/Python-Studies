# -*- coding: utf-8 -*-
"""
Define the JSON loader interface
"""

# Import python libs
import json
import pop.hub

__virtualname__ = "json"
__contracts__ = [__virtualname__]


def __virtual__(hub):
    return True


def load(hub: "pop.hub.Hub", path):
    """
    Use json to read in a file
    """
    try:
        with open(path, "r") as fp_:
            ret = json.loads(fp_.read())
        return ret
    except FileNotFoundError:
        return {}


def render(hub: "pop.hub.Hub", val):
    """
    Take the string and render it in json
    """
    return json.loads(val)
