"""
The input module is used to translate typical input strings into the
ref/args/kwargs used by pop when forwarding data into functions.
"""
# Import python libs
import re
from typing import Any, Dict, List, Tuple

# Import third party libs
import yaml
import pop.hub

KWARG_REGEX = re.compile(r"^([^\d\W][\w.-]*)=(?!=)(.*)$", re.UNICODE)


def parse(
    hub: "pop.hub.Hub",
    args: List[Any],
    condition: bool = True,
    no_parse: Tuple[str] = None,
) -> Tuple[List[Any], Dict[str, Any]]:
    """
    Parse out the args and kwargs from a list of input values. Optionally,
    return the args and kwargs without passing them to condition_input().
    Don't pull args with key=val apart if it has a newline in it.
    """
    if no_parse is None:
        no_parse = ()
    _args = []
    _kwargs = {}
    for arg in args:
        if isinstance(arg, str):
            if "=" in arg:
                arg_name, arg_value = _parse_kwarg(arg)
                if arg_name:
                    _kwargs[arg_name] = (
                        _yamlify_arg(arg_value)
                        if arg_name not in no_parse
                        else arg_value
                    )
            else:
                _args.append(_yamlify_arg(arg))
        elif isinstance(arg, dict):
            # Yes, we're popping this key off and adding it back if
            # condition_input is called below, but this is the only way to
            # gracefully handle both CLI and API input.
            if arg.pop("__kwarg__", False) is True:
                _kwargs.update(arg)
            else:
                _args.append(arg)
        else:
            _args.append(arg)
    if condition:
        return _condition_input(_args, _kwargs)
    return _args, _kwargs


def _yamlify_arg(arg: Any) -> Any:
    """
    yaml.safe_load the arg
    """
    if not isinstance(arg, str):
        return arg

    if arg.strip() == "":
        # Because YAML loads empty (or all whitespace) strings as None, we
        # return the original string
        # >>> import yaml
        # >>> yaml.load('') is None
        # True
        # >>> yaml.load('      ') is None
        # True
        return arg

    elif "_" in arg and all([x in "0123456789_" for x in arg.strip()]):
        # When the stripped string includes just digits and underscores, the
        # underscores are ignored and the digits are combined together and
        # loaded as an int. We don't want that, so return the original value.
        return arg

    try:
        original_arg = arg
        if "#" in arg:
            # Only yamlify if it parses into a non-string type, to prevent
            # loss of content due to # as comment character
            parsed_arg = yaml.safe_load(arg)
            if isinstance(parsed_arg, str) or parsed_arg is None:
                return arg
            return parsed_arg
        if arg == "None":
            arg = None
        else:
            arg = yaml.safe_load(arg)

        if isinstance(arg, dict):
            # dicts must be wrapped in curly braces
            if isinstance(original_arg, str) and not original_arg.startswith("{"):
                return original_arg
            else:
                return arg

        elif isinstance(arg, list):
            # lists must be wrapped in brackets
            if isinstance(original_arg, str) and not original_arg.startswith("["):
                return original_arg
            else:
                return arg

        elif arg is None or isinstance(arg, (list, float, int, str)):
            # yaml.safe_load will load '|' as '', don't let it do that.
            if arg == "" and original_arg in ("|",):
                return original_arg
            # yaml.safe_load will treat '#' as a comment, so a value of '#'
            # will become None. Keep this value from being stomped as well.
            elif arg is None and original_arg.strip().startswith("#"):
                return original_arg
            else:
                return arg
        else:
            # we don't support this type
            return original_arg
    except Exception:
        # In case anything goes wrong...
        return original_arg


def _parse_kwarg(string_: str) -> Tuple:
    """
    Parses the string and looks for the following kwarg format:
    "{argument name}={argument value}"
    For example: "my_message=Hello world"
    Returns the kwarg name and value, or (None, None) if the regex was not
    matched.
    """
    try:
        return KWARG_REGEX.match(string_).groups()
    except AttributeError:
        return None, None


def _condition_input(args: List[Any], kwargs: Dict[str, Any]) -> List[str]:
    """
    Return a single arg structure for the publisher to safely use
    """
    ret = []
    for arg in args:
        if isinstance(arg, int):
            ret.append(str(arg))
        else:
            ret.append(arg)
    if isinstance(kwargs, dict) and kwargs:
        kw_ = {"__kwarg__": True}
        for key, val in kwargs.items():
            kw_[key] = val
        return ret + [kw_]
    return ret
