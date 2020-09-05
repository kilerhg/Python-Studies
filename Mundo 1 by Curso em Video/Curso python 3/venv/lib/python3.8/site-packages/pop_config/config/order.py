def apply(hub, raw, raw_cli, cli, cli_args, os_vars, configs):
    # Defaults (raw)
    # Config files (configs)
    # OS (os_vars)
    # CLI (cli_args)
    ret = {}
    for imp in raw:
        ret[imp] = {}
        for key, data in raw[imp]["CONFIG"].items():
            if "default" in data:
                ret[imp][key] = data["default"]
    # TODO: This assumes that we are using the namespace approach,
    # This makes the config structure the easiest, meaning that components are
    # namespaced by the user.
    # Some other additional pattern could be added and this chunk could
    # be made pluggable.
    for imp in configs:
        if imp not in ret:
            ret[imp] = {}
        for key in configs[imp]:
            ret[imp][key] = configs[imp][key]
    for imp in os_vars:
        for key in os_vars[imp]:
            ret[imp][key] = os_vars[imp][key]
    for key in cli_args:
        if key in raw_cli:
            if "source" in raw_cli[key]:
                ret[raw_cli[key]["source"]][key] = cli_args[key]
            else:
                ret[cli][key] = cli_args[key]
    return ret
