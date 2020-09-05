def __init__(hub):
    """
    Load the subdirs for conf
    """
    hub.pop.sub.add(dyne_name="log")
    hub.pop.sub.load_subdirs(hub.config, recurse=True)
    hub.config.ARGS = {}
    hub.config.SECTIONS = ("CONFIG", "CLI_CONFIG", "SUBCOMMANDS", "DYNE")
    hub.config.CONFIG_SECTIONS = ("CONFIG", "CLI_CONFIG")
