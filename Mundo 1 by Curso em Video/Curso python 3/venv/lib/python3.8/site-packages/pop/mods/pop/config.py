import pop.hub
from typing import List


def load(
    hub: "pop.hub.Hub",
    sources: List[str],
    cli: str = None,
    dyne_name: str = None,
    loader: str = "yaml",
    parse_cli: bool = True,
):
    """
    Use the pop-config system to load up a fresh configuration for this project
    from the included conf.py file.
    """
    hub.pop.sub.add(dyne_name="config")
    hub.config.integrate.load(sources, cli, dyne_name, loader, parse_cli)
