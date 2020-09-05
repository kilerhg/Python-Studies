# -*- coding: utf-8 -*-
"""
Define the yaml loader interface
"""

# Import third party libs
try:
    import toml

    HAS_TOML = True
except ImportError:
    HAS_TOML = False

__virtualname__ = "toml"
# __contracts__ = [__virtualname__]


def __virtual__(hub):
    if HAS_TOML:
        return True
    return (False, "TOML could not be loaded")


def load(hub, path):
    """
    use toml to read in a file
    """
    try:
        with open(path, "rb") as fp_:
            return toml.load(fp_.read())
    except FileNotFoundError:
        pass
    return {}


def render(hub, val):
    """
    Take the string and render it in json
    """
    return toml.loads(val)
