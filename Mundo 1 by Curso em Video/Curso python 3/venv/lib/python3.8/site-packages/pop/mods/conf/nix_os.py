"""
The os module is used to gather configuration options from the OS facility
to send configuration options into applications. In the case of Unix like
systems this translates to the environment variables. On Windows systems
this translates to the registry.
"""
# Import python libs
import os
import pop.hub

__virtualname__ = "os"


def __virtual__(hub):
    """
    Don't load on Windows, this is for *nix style platforms
    """
    # TODO: detect if windows
    return True


def gather(hub: "pop.hub.Hub", defaults):
    """
    Iterate over the default config data and look for os: True/str options. When set
    gather the option from environment variables is present
    """
    ret = {}
    for key in defaults:
        if not "os" in defaults[key]:
            continue
        os_var = defaults[key]["os"]
        if os_var is True:
            os_var = key
        os_var = os_var.upper()
        if os_var in os.environ:
            ret[key] = os.environ[os_var]
    return ret
