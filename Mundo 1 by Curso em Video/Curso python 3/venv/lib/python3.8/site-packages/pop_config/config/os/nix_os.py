"""
Read in keys from *NIX like oses - AKA Environement variables
"""
# Import python libs
import os

__virtualname__ = "system"


def __virtual__(hub):
    """
    Don't load on Windows, this is for *nix style platforms
    """
    # TODO: detect if not windows
    return True


def collect(hub, key):
    """
    Collect the option from environment variable if present
    """
    ret = {}
    key = key.upper()
    if key in os.environ:
        return os.environ[key]
    return None
