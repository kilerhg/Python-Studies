"""
Routines to verify the working environment etc.
"""
# Import python libs
import os
import pop.hub


def env(hub: "pop.hub.Hub"):
    """
    Verify that the directories specified in the system exist
    """
    for key in hub.opts:
        if key.endswith("_dir"):
            try:
                os.makedirs(hub.opts[key])
            except OSError:
                pass
