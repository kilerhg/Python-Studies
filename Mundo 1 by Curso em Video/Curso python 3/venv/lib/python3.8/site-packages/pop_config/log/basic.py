import logging


def setup(hub, conf):
    """
    Given the configuration data set up the logger
    """
    # Use the saved root logger
    root = logging.getLogger()

    raw_level = conf["log_level"].strip().lower()
    if raw_level.isdigit():
        hub.log.INT_LEVEL = int(raw_level)
    else:
        hub.log.INT_LEVEL = hub.log.LEVEL.get(raw_level, root.level)

    root.setLevel(hub.log.INT_LEVEL)
    cf = logging.Formatter(fmt=conf["log_fmt_console"], datefmt=conf["log_datefmt"])
    ch = logging.StreamHandler()
    ch.setLevel(hub.log.INT_LEVEL)
    ch.setFormatter(cf)
    root.addHandler(ch)

    ff = logging.Formatter(fmt=conf["log_fmt_console"], datefmt=conf["log_datefmt"])
    fh = logging.FileHandler(conf["log_file"])
    fh.setFormatter(ff)
    root.addHandler(fh)
