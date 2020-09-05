import yaml


def yamlify_arg(arg):
    """
    yaml.safe_load the arg
    """
    if not isinstance(arg, str):
        return arg

    # YAML loads empty (or all whitespace) strings as None:
    #
    # >>> import yaml
    # >>> yaml.load('') is None
    # True
    # >>> yaml.load('      ') is None
    # True
    #
    # Similarly, YAML document start/end markers would not load properly if
    # passed through PyYAML, as loading '---' results in None and '...' raises
    # an exception.
    #
    # Therefore, skip YAML loading for these cases and just return the string
    # that was passed in.
    if arg.strip() in ("", "---", "..."):
        return arg

    elif "_" in arg and all([x in "0123456789_" for x in arg.strip()]):
        # When the stripped string includes just digits and underscores, the
        # underscores are ignored and the digits are combined together and
        # loaded as an int. We don't want that, so return the original value.
        return arg

    else:
        if any(np_char in arg for np_char in ("\t", "\r", "\n")):
            # Don't mess with this CLI arg, since it has one or more
            # non-printable whitespace char. Since the CSafeLoader will
            # sanitize these chars rather than raise an exception, just
            # skip YAML loading of this argument and keep the argument as
            # passed on the CLI.
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
            # yaml.safe_load will load '|' and '!' as '', don't let it do that.
            if arg == "" and original_arg in ("|", "!"):
                return original_arg
            # yaml.safe_load will treat '#' as a comment, so a value of '#'
            # will become None. Keep this value from being stomped as well.
            elif arg is None and original_arg.strip().startswith("#"):
                return original_arg
            # Other times, yaml.safe_load will load '!' as None. Prevent that.
            elif arg is None and original_arg == "!":
                return original_arg
            else:
                return arg
        else:
            # we don't support this type
            return original_arg
    except Exception:  # pylint: disable=broad-except
        # In case anything goes wrong...
        return original_arg
