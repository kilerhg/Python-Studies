"""
Find the conf.py files specified in sources
"""
# Import python libs
import importlib
import copy
import os


def _load_pyimp(hub, imp):
    """
    Load up a python path, parse it and return the conf dataset
    """
    ret = {imp: {}}
    cmod = importlib.import_module(f"{imp}.conf")
    path = os.path.dirname(cmod.__file__)
    for sec in hub.config.SECTIONS:
        ret[imp][sec] = copy.deepcopy(getattr(cmod, sec, {}))
    return path, ret


def load(hub, sources, dyne_names, cli):
    """
    Look over the sources list and find the correct conf.py files
    """
    # Dynamic names
    # First gather the defined sources, they are the authoritative ones
    # Then detect what the dynamic names are in the source
    # Merged the sources dyne names with any passed dyne names
    # Load up and extend the raw with all of the dynamic names
    raw = {}
    dyne = hub.pop.dyne.get()
    if not isinstance(sources, list):
        sources = [sources]
    for source in sources:
        try:
            path, data = _load_pyimp(hub, source)
        except ImportError:
            continue
        hub.pop.dicts.update(raw, data)
    dnames = set(dyne_names)
    for source in raw:
        for dname in raw[source]["DYNE"]:
            dnames.add(dname)
    for name in dnames:
        if name in dyne:
            if name not in raw:
                raw[name] = {"CONFIG": {}, "CLI_CONFIG": {}}
            if "CONFIG" in dyne[name]:
                config_draw = {}
                for key, val in dyne[name]["CONFIG"].items():
                    new_dyne = val.get("dyne")
                    if new_dyne == "__cli__":
                        new_dyne = cli
                    if new_dyne:
                        val["source"] = new_dyne
                        config_draw[key] = val
                        if (
                            key in dyne[name]["CLI_CONFIG"]
                            and "dyne" not in dyne[name]["CLI_CONFIG"][key]
                        ):
                            dyne[name]["CLI_CONFIG"][key]["dyne"] = new_dyne
                hub.pop.dicts.update(raw[cli]["CONFIG"], config_draw)
            if "CLI_CONFIG" in dyne[name]:
                cli_draw = {}
                for key, val in dyne[name]["CLI_CONFIG"].items():
                    new_dyne = val.get("dyne")
                    if new_dyne == "__cli__":
                        new_dyne = cli
                    if new_dyne:
                        val["source"] = new_dyne
                        cli_draw[key] = val
                hub.pop.dicts.update(raw[cli]["CLI_CONFIG"], cli_draw)
    return raw


def verify(hub, opts):
    """
    Verify that the environment and all named directories in the
    configuration exist
    """
    for imp in opts:
        for key in opts[imp]:
            if key == "root_dir":
                continue
            if key == "config_dir":
                continue
            if key.endswith("_dir"):
                if not os.path.isdir(opts[imp][key]):
                    os.makedirs(opts[imp][key])
