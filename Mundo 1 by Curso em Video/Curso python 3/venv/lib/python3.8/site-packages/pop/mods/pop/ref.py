"""
Used to resolve resolutions to paths on the hub
"""
import pop.hub
from typing import List


def last(hub: "pop.hub.Hub", ref: str) -> "pop.hub.Sub":
    """
    Takes a string that references the desired ref and returns the last object
    called out in that ref
    """
    return hub.pop.ref.path(ref)[-1]


def path(hub: "pop.hub.Hub", ref: str) -> List["pop.hub.Sub"]:
    """
    Retuns a list of references up to the named ref
    """
    ret = [hub]
    if isinstance(ref, str):
        ref = ref.split(".")
    for chunk in ref:
        ret.append(getattr(ret[-1], chunk))
    return ret


def create(hub: "pop.hub.Hub", ref: str, obj: object):
    """
    Create an attribute at a given target using just a ref string and the
    object to be saved at said location. The desired location must already
    exist!

    :param hub: The redistributed pop central hub
    :param ref: The dot delimited string referencing the target location to
        create the given object on the hub
    :param obj: The object to store at the given reference point
    """
    if "." not in ref:
        setattr(hub, ref, obj)
        return
    comps = ref.split(".")
    sub_ref = ref[: ref.rindex(".")]
    var = comps[-1]
    top = hub.pop.ref.last(sub_ref)
    setattr(top, var, obj)
