def __init__(hub):
    """
    Load the subdirs for conf
    """
    hub.__._mem = {}
    hub.pop.sub.load_subdirs(hub.conf)
