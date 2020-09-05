from typing import Dict, List


def to_num(text: str) -> int or float:
    """
    Convert a string to a number.
    Returns an integer if the string represents an integer, a floating
    point number if the string is a real number, or the string unchanged
    otherwise.
    """
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            return text


def to_dict(data: List[str], key: str) -> Dict:
    """
    Convert MySQL-style output to a python dictionary
    """
    ret = {}
    headers = [""]
    for line in data:
        if not line:
            continue
        if line.startswith("+"):
            continue
        comps = line.split("|")
        for comp in range(len(comps)):
            comps[comp] = comps[comp].strip()
        if len(headers) > 1:
            index = len(headers) - 1
            row = {}
            for field in range(index):
                if field < 1:
                    continue
                row[headers[field]] = to_num(comps[field])
            ret[row[key]] = row
        else:
            headers = comps
    return ret
