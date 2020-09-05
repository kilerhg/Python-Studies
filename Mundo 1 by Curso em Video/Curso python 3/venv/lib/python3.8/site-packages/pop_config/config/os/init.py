"""
The os sub is used to gather configuration options from the OS facility
to send configuration options into applications.
"""
# Import python libs
import os


def gather(hub, raw):
    """
    Collect the keys that need to be found and pass them to the
    os specific loaded plugin
    """
    ret = {}
    for imp in raw:
        for sec in hub.config.CONFIG_SECTIONS:
            if sec not in raw[imp]:
                continue
            for key in raw[imp][sec]:
                osvar = raw[imp][sec][key].get("os", None)
                if osvar is not None:
                    val = hub.config.os.system.collect(osvar)
                    if val is not None:
                        src = raw[imp][sec][key].get("source", imp)
                        if src not in ret:
                            ret[src] = {}
                        ret[src][key] = val
    return ret
