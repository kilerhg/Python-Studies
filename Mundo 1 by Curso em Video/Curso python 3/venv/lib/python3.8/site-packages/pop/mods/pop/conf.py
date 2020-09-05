"""
Convenience wrappers to make using the conf system as easy and seamless as possible
"""
import pop.hub
from typing import Any, Dict, List


def integrate(
    hub: "pop.hub.Hub",
    imports: List[str] or str,
    override: Dict[str, Any] = None,
    cli: str = None,
    roots: bool = None,
    loader: str = "json",
    logs: bool = True,
):
    """
    Load the conf sub and run the integrate sequence.
    """
    hub.pop.sub.add("pop.mods.conf")
    hub.conf.integrate.load(
        imports, override, cli=cli, roots=roots, loader=loader, logs=logs
    )
