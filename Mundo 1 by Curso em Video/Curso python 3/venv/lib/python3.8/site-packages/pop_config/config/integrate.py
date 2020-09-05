from typing import List


def load(
    hub,
    sources: List[str],
    cli: str = None,
    dyne_names: List[str] = None,
    loader: str = "yaml",
    parse_cli: bool = True,
    logs: bool = True,
):
    """
    Load up the configs from the integrate system
    """
    if not isinstance(sources, list):
        sources = [sources]
    sources.append("pop_config")
    if dyne_names is None:
        dyne_names = []
    raw = hub.config.dirs.load(sources, dyne_names, cli)
    os_vars = hub.config.os.init.gather(raw)
    cli_args, raw_cli = hub.config.args.gather(raw, cli, parse_cli)
    if cli_args.get("version"):
        hub.config.version.run(cli)
    configs = hub.config.file.init.parse(raw, cli, os_vars, cli_args, loader)
    opt = hub.config.order.apply(raw, raw_cli, cli, cli_args, os_vars, configs)
    hub.OPT = hub.pop.data.imap(opt)

    if logs:
        log_plugin = hub.OPT[sources[0]].get("log_plugin")
        getattr(hub, f"log.{log_plugin}.setup")(hub.OPT[sources[0]])
