"""
Seed a new project with a directory tree and first files
"""
# Import python libs
import os
import pop.hub

SETUP = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import python libs
import os
import shutil
from setuptools import setup, Command

NAME = "%%NAME%%"
DESC = ""

# Version info -- read without importing
_locals = {}
with open("{}/version.py".format(NAME)) as fp:
    exec(fp.read(), None, _locals)
VERSION = _locals["version"]
SETUP_DIRNAME = os.path.dirname(__file__)
if not SETUP_DIRNAME:
    SETUP_DIRNAME = os.getcwd()

with open("README.rst", encoding="utf-8") as f:
    LONG_DESC = f.read()

with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()


class Clean(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for subdir in (NAME, "tests"):
            for root, dirs, files in os.walk(
                os.path.join(os.path.dirname(__file__), subdir)
            ):
                for dir_ in dirs:
                    if dir_ == "__pycache__":
                        shutil.rmtree(os.path.join(root, dir_))


def discover_packages():
    modules = []
    for package in (NAME,):
        for root, _, files in os.walk(os.path.join(SETUP_DIRNAME, package)):
            pdir = os.path.relpath(root, SETUP_DIRNAME)
            modname = pdir.replace(os.sep, ".")
            modules.append(modname)
    return modules


setup(
    name=NAME,
    author="",
    author_email="",
    url="",
    version=VERSION,
    install_requires=REQUIREMENTS,
    description=DESC,
    long_description=LONG_DESC,
    long_description_content_type="text/x-rst",
    python_requires=">=3.6",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 5 - Production/Stable",
    ],
    packages=discover_packages(),
    entry_points={"console_scripts": ["%%NAME%% = %%NAME%%.scripts:start",],},
    cmdclass={"clean": Clean},
)
"""

PYPROJ = r"""[tool.black]
line-length = 88
target-version = ['py36', 'py37', 'py38']
include = '\.pyi?$'
exclude = '''
(
  /(
      \.eggs
    | \.git
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | _build
    | buck-out
    | build
    | dist
  )/
)
'''
"""

PRECOM = r"""---
minimum_pre_commit_version: 1.15.2
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.5.0
    hooks:
      - id: check-merge-conflict  # Check for files that contain merge conflict strings.
        language_version: python3
      - id: trailing-whitespace   # Trims trailing whitespace.
        args: [--markdown-linebreak-ext=md]
        language_version: python3
      - id: mixed-line-ending     # Replaces or checks mixed line ending.
        args: [--fix=lf]
        language_version: python3
      - id: end-of-file-fixer     # Makes sure files end in a newline and only a newline.
        exclude: tests/fake_.*\.key
        language_version: python3
      - id: check-ast             # Simply check whether files parse as valid python.
        language_version: python3
      - id: check-yaml
      - id: check-json
  -   repo: https://github.com/psf/black
      rev: 19.10b0
      hooks:
      - id: black
        language_version: python3
"""

ENTRY = """entry_points={
        'console_scripts': [
            '%%NAME%% = %%NAME%%.scripts:start',
            ],
          },"""

SCRIPT = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pop.hub


def start():
    hub = pop.hub.Hub()
    hub.pop.sub.add(dyne_name="%%NAME%%")
    hub.%%NAME%%.init.cli()
"""

INIT = """def __init__(hub):
    # Remember not to start your app in the __init__ function
    # This function should just be used to set up the plugin subsystem
    # Add another function to call from your run.py to start the app
    pass


def cli(hub):
    hub.pop.config.load(["%%NAME%%"], cli="%%NAME%%")
    print("%%NAME%% works!")
"""

REQ = "pop\n"

CONF = """CLI_CONFIG = {}
CONFIG = {}
SUBCOMMANDS = {}
DYNE = {
    "%%NAME%%": ["%%NAME%%"],
%%DYNE%%}
"""

VER = """# -*- coding: utf-8 -*-
version = "1"\n
"""


def new(hub: "pop.hub.Hub"):
    """
    Given the option in hub.opts "seed_name" create a directory tree for a
    new pop project
    """
    hub.PATH = os.getcwd()
    name = hub.opts["seed_name"]
    for dyne in hub.opts["dyne"]:
        hub.pop.seed.mkdir(name, dyne)
        hub.pop.seed.mkdir(name, dyne, "contracts")
    if hub.opts["type"] == "v":
        hub.pop.seed.mkdir(name)
        hub.pop.seed.mksetup(name, entry=False)
        hub.pop.seed.mkversion(name)
        hub.pop.seed.mkconf(name)
        hub.pop.seed.mkreq(name)
        hub.pop.seed.mkreadme(name)
    else:
        hub.pop.seed.mkdir(name, name)
        hub.pop.seed.mkdir(name, name, "contracts")
        hub.pop.seed.mksetup(name)
        hub.pop.seed.mkscript(name)
        hub.pop.seed.mkversion(name)
        hub.pop.seed.mkconf(name)
        hub.pop.seed.mkreq(name)
        hub.pop.seed.mkrun(name)
        hub.pop.seed.mkinit(name)
        hub.pop.seed.mkreadme(name)
    hub.pop.seed.mkproj()
    hub.pop.seed.mkprecom()
    hub.pop.seed.print_post(name)


def mkdir(hub: "pop.hub.Hub", *args):
    """
    Create the named dir
    """
    path = hub.PATH
    for dir_ in args:
        path = os.path.join(path, dir_)
        if not os.path.isdir(path):
            try:
                os.makedirs(path)
            except Exception:
                print("Failed to make {}".format(path))
                continue
            if dir_ == "scripts" and len(args) == 1:
                continue


def mkreq(hub: "pop.hub.Hub", name: str):
    path = os.path.join(hub.PATH, "requirements.txt")
    with open(path, "w+") as fp:
        fp.write(REQ)


def mksetup(hub: "pop.hub.Hub", name: str, entry: bool = True):
    """
    Create and write out a setup.py file
    """
    path = os.path.join(hub.PATH, "setup.py")
    setup_str = SETUP.replace("%%NAME%%", name)
    if entry:
        setup_str = setup_str.replace(
            "%%ENTRY%%",
            ENTRY.replace(
                "%%NAME%%.scripts:start", f"{name.replace('-', '_')}.scripts:start"
            ),
        )
        setup_str = setup_str.replace("%%ENTRY%%", ENTRY.replace("%%NAME%%", name))
    else:
        setup_str = setup_str.replace("%%ENTRY%%", "")
    with open(path, "w+") as fp:
        fp.write(setup_str)


def mkscript(hub: "pop.hub.Hub", name: str):
    """
    Create and write out a setup.py file
    """
    path = os.path.join(hub.PATH, name, "scripts.py")
    script_str = SCRIPT.replace("%%NAME%%", name)
    with open(path, "w+") as fp:
        fp.write(script_str)


def mkrun(hub: "pop.hub.Hub", name: str):
    """
    Create the convenience run.py script allowing the project to
    be executed from the local directory
    """
    path = os.path.join(hub.PATH, "run.py")
    run_str = SCRIPT.replace("%%NAME%%", name)
    run_str += "\n\nstart()\n"
    with open(path, "w+") as fp:
        fp.write(run_str)


def mkinit(hub: "pop.hub.Hub", name: str):
    """
    Create the intial init.py
    """
    path = os.path.join(hub.PATH, name, name, "init.py")
    init_str = INIT.replace("%%NAME%%", name)
    with open(path, "w+") as fp:
        fp.write(init_str)


def mkversion(hub: "pop.hub.Hub", name: str):
    """
    Create the version.py file
    """
    path = os.path.join(hub.PATH, name, "version.py")
    with open(path, "w+") as fp:
        fp.write(VER)


def mkconf(hub: "pop.hub.Hub", name: str):
    """
    Create the version.py file
    """
    path = os.path.join(hub.PATH, name, "conf.py")
    dyne_str = ""
    for dyne in hub.opts["dyne"]:
        dyne_str += f"        '{dyne}': ['{dyne}'],\n"
    conf_str = CONF.replace("%%NAME%%", name)
    conf_str = conf_str.replace("%%DYNE%%", dyne_str)
    with open(path, "w+") as fp:
        fp.write(conf_str)


def mkreadme(hub: "pop.hub.Hub", name: str):
    """
    Create and write out a setup.py file
    """
    path = os.path.join(hub.PATH, "README.rst")
    eqchars = "=" * len(name)
    readme_str = f"{eqchars}\n{name.upper()}\n{eqchars}\n"
    with open(path, "w+") as fp:
        fp.write(readme_str)


def mkproj(hub: "pop.hub.Hub"):
    """
    Create the pyproject.toml file
    """
    path = os.path.join(hub.PATH, "pyproject.toml")
    with open(path, "a+") as fp:
        fp.write(PYPROJ)


def mkprecom(hub: "pop.hub.Hub"):
    """
    Create the precommit file
    """
    path = os.path.join(hub.PATH, ".pre-commit-config.yaml")
    with open(path, "w+") as fp:
        fp.write(PRECOM)


def print_post(hub: "pop.hub.Hub", name: str):
    """
    Print a message after the run to document how to enable
    things like pre-commit
    """
    print(f"Congratulations! You now have a project set up called {name}!")
    print("This project can be executed by calling the run.py script:")
    print("    python3 run.py")
    print(
        "This project has been set up with pre-commit hooks for code checks and black."
    )
    print('First set up your source control environment with "git init" or "hg init".')
    print("Then enable these checks in your git checkout:")
    print("    pip install pre-commit")
    print("    pre-commit install")
    print("To run pre-commit manually, execute:")
    print("    pre-commit run --all-files")
