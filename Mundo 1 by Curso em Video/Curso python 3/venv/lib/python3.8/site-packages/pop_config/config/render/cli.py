# -*- coding: utf-8 -*-
from typing import Any, Dict, List

try:
    import yaml

    HAS_YAML = True
except ImportError:
    HAS_YAML = False

__virtualname__ = "cli"


def __virtual__(hub):
    if HAS_YAML:
        return True
    return (False, "PyYaml could not be loaded")


def load(hub, path):
    try:
        with open(path, "rb") as fp_:
            ret = {}
            for line in fp_:
                ret.update(hub.config.render.cli.render(line))
            return ret
    except FileNotFoundError:
        pass
    return {}


def render(hub, val: List[str] or str) -> List[str]:
    """
    Take the string and render it in json
    """
    ret = []
    if isinstance(val, str):
        val = [val]
    for v in val:
        if "=" in v:
            key, v = v.split("=", maxsplit=1)
            ret.append({key: yaml.safe_load(v)})
        else:
            ret.append(yaml.safe_load(v))

    return ret
