"""
Used to take care of the options that end in `_dir`. The assumption is that
`_dir` options need to be treated differently. They need to verified to exist
and they need to be rooted based on the user, root option etc.
"""
# Import python libs
import os
import pop.hub


def roots(hub: "pop.hub.Hub", default_root, f_opts, root_dir):
    """
    Detect the root dir data and apply it
    """
    os_root = os.path.abspath(os.sep)
    root = os_root
    change = False
    non_priv = False
    if hasattr(os, "geteuid"):
        if not os.geteuid() == 0:
            change = True
            non_priv = True
    if root_dir and root_dir != default_root:
        root = root_dir
        change = True
    if not root.endswith(os.sep):
        root = f"{root}{os.sep}"
    if change:
        for imp in f_opts:
            for key in f_opts[imp]:
                if key == "root_dir":
                    continue
                if key.endswith("_dir"):
                    if non_priv:
                        root = os.path.join(os.environ["HOME"], f".{imp}{os.sep}")
                    if imp in f_opts[imp][key]:
                        a_len = len(imp) + 1
                        f_opts[imp][
                            key
                        ] = f"{os_root}{f_opts[imp][key][f_opts[imp][key].index(imp)+a_len:]}"
                    f_opts[imp][key] = f_opts[imp][key].replace(os_root, root, 1)


def verify(hub: "pop.hub.Hub", opts):
    """
    Verify that the environment and all named directories in the
    configuration exist
    """
    for key in opts:
        if key == "root_dir":
            continue
        if key == "config_dir":
            continue
        if key.endswith("_dir"):
            if not os.path.isdir(opts[key]):
                os.makedirs(opts[key])
