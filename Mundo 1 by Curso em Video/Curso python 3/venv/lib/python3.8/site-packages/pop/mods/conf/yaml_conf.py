# -*- coding: utf-8 -*-
"""
Define the yaml loader interface
"""

# Import third party libs
import pop.hub

try:
    import yaml

    HAS_YAML = True
except ImportError:
    HAS_YAML = False

__virtualname__ = "yaml"
__contracts__ = [__virtualname__]


def __virtual__(hub):
    if HAS_YAML:
        return True
    return (False, "PyYaml could not be loaded")


def load(hub: "pop.hub.Hub", path):
    """
    use yaml to read in a file
    """
    try:
        with open(path, "rb") as fp_:
            return yaml.safe_load(fp_.read())
    except FileNotFoundError:
        pass
    return {}


def render(hub: "pop.hub.Hub", val):
    """
    Take the string and render it in json
    """
    return yaml.safe_load(val)
