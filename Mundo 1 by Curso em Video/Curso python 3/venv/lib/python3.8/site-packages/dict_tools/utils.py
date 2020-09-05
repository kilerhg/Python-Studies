from typing import ByteString, Dict, Iterable, Mapping, Text


def decode_dict(data: Dict[bytes, bytes]) -> Dict[str, str]:
    """
    Recursively decode all byte-strings found in a dictionary
    """
    ret = {}
    for key, value in data.items():
        if isinstance(key, ByteString):
            key = key.decode()
        if isinstance(value, (Mapping, Dict)):
            ret[key] = decode_dict(value)
        elif isinstance(value, ByteString):
            ret[key] = value.decode()
        elif isinstance(value, Iterable) and not isinstance(value, Text):
            ret[key] = value.__new__(
                x.decode() if isinstance(x, ByteString) else x for x in value
            )
        else:
            ret[key] = value
    return ret
