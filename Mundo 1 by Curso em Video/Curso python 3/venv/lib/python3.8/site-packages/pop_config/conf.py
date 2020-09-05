import os
import sys

CLI_CONFIG = {
    "log_file": {"dyne": "__cli__"},
    "log_level": {"dyne": "__cli__"},
    "log_fmt_logfile": {"dyne": "__cli__"},
    "log_fmt_console": {"dyne": "__cli__"},
    "log_datefmt": {"dyne": "__cli__"},
    "log_plugin": {"dyne": "__cli__"},
}

CONFIG = {
    "log_file": {
        "dyne": "__cli__",
        "default": f"{os.path.splitext(os.path.split(sys.argv[0])[1])[0]}.log",
        "help": "The location of the log file",
        "group": "Logging Options",
    },
    "log_level": {
        "dyne": "__cli__",
        "default": "warning",
        "help": "Set the log level, either quiet, info, warning, or error",
        "group": "Logging Options",
    },
    "log_fmt_logfile": {
        "dyne": "__cli__",
        "default": "%(asctime)s,%(msecs)03d [%(name)-17s][%(levelname)-8s] %(message)s",
        "help": "The format to be given to log file messages",
        "group": "Logging Options",
    },
    "log_fmt_console": {
        "dyne": "__cli__",
        "default": "[%(levelname)-8s] %(message)s",
        "help": "The log formatting used in the console",
        "group": "Logging Options",
    },
    "log_datefmt": {
        "dyne": "__cli__",
        "default": "%H:%M:%S",
        "help": "The date format to display in the logs",
        "group": "Logging Options",
    },
    "log_plugin": {
        "dyne": "__cli__",
        "default": "basic",
        "help": "The logging plugin to use",
        "group": "Logging Options",
    },
}
SUBCOMMANDS = {}
DYNE = {
    "config": ["config"],
    "log": ["log"],
}
