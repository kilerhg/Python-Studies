#!/usr/bin/python3

import pop.hub


def pop_seed():
    CONFIG = {
        "seed_name": {
            "positional": True,
            "help": "The name of the project that is being created",
        },
        "type": {
            "default": "p",
            "options": ["-t"],
            "help": 'The type of project to build, by default make a standalone project, but for a vetical app project pass a "v"',
        },
        "dyne": {
            "options": ["-d"],
            "default": [],
            "nargs": "*",
            "help": "A space delimited list of additional dynamic names for vertical app-merging",
        },
    }

    hub = pop.hub.Hub()
    hub.pop.sub.add("pop.mods.conf")
    hub.opts = hub.conf.reader.read(CONFIG)
    hub.pop.seed.new()
