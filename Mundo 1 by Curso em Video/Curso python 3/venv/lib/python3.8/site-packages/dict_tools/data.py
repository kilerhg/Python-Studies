import copy
import fnmatch
import logging
import re
import yaml

from . import DEFAULT_TARGET_DELIM
from . import args
from collections.abc import Mapping, MutableMapping, Sequence
from typing import Any, Dict, Iterable, List, Set

log = logging.getLogger(__name__)


class CaseInsensitiveDict(MutableMapping):
    """
    Inspired by requests' case-insensitive dict implementation, but works with
    non-string keys as well.
    """

    def __init__(self, init=None, **kwargs):
        """
        Force internal dict to be ordered to ensure a consistent iteration
        order, irrespective of case.
        """
        self._data = {}
        self.update(init or {}, **kwargs)

    def __len__(self):
        return len(self._data)

    def __setitem__(self, key, value):
        # Store the case-sensitive key so it is available for dict iteration
        self._data[to_lowercase(key)] = (key, value)

    def __delitem__(self, key):
        del self._data[to_lowercase(key)]

    def __getitem__(self, key):
        return self._data[to_lowercase(key)][1]

    def __iter__(self):
        return (item[0] for item in self._data.values())

    def __eq__(self, rval):
        if not isinstance(rval, Mapping):
            # Comparing to non-mapping type (e.g. int) is always False
            return False
        return dict(self.items_lower()) == dict(CaseInsensitiveDict(rval).items_lower())

    def __repr__(self):
        return repr(dict(self.items()))

    def items_lower(self):
        """
        Returns a generator iterating over keys and values, with the keys all
        being lowercase.
        """
        return ((key, val[1]) for key, val in self._data.items())

    def copy(self):
        """
        Returns a copy of the object
        """
        return CaseInsensitiveDict(self._data.items())


class ImmutableDict(Mapping):
    """
    An abstract base class that implements the interface of a `dict` but is immutable.
    Items can be retrieved via namespacing.
    No values can be changed after initialization
    """

    def __init__(self, init_: Dict[str, Any], **c_kwargs):
        """
        :param init_: A dictionary from which to inherit data
        """
        init_.update(**c_kwargs)
        values = {}
        for k, v in init_.items():
            if isinstance(v, Dict):
                values[k] = ImmutableDict(init_=v)
            elif isinstance(v, (tuple, int, str, bytes)):
                values[k] = v
            elif isinstance(v, Iterable):
                values[k] = tuple(v)
            else:
                values[k] = v
        # __setattr__ is borked (on purpose) so we have to call it from super() right here
        super().__setattr__("_ImmutableDict__store", values)

    def __setattr__(self, k: str, v: Any):
        raise TypeError(
            f"{self.__class__.__name__} does not support attribute assignment"
        )

    def __getattr__(self, k: str):
        return self.__store[k]

    def __getitem__(self, k: str) -> Any:
        return self.__store[k]

    def __contains__(self, k: str) -> bool:
        return k in self.__store

    def __iter__(self):
        return iter(self.__store)

    def __len__(self) -> int:
        return len(self.__store.keys())

    def __copy__(self) -> Dict[str, Any]:
        ret = {}
        # Unpack IMAP items so that it's turtles all the way down
        for k, v in self.__store.items():
            if isinstance(v, ImmutableDict):
                ret[k] = v.__copy__()
            else:
                ret[k] = v
        return ret

    def __repr__(self):
        return repr(copy.copy(self))


class NamespaceDict(dict):
    """
    A dictionary that can access it's string keys through the namespace
    """

    def __init__(self, seq: Iterable = None, **kwargs):
        """
        NamespaceDict() -> new empty namespaced dictionary
        NamespaceDict(mapping) -> new namespaced dictionary initialized from a mapping object's
            (key, value) pairs
        NamespaceDict(iterable) -> new namespaced dictionary initialized as if via:
            d = {}
            for k, v in iterable:
                d[k] = v
        NamespaceDict(**kwargs) -> new namespaced dictionary initialized with the name=value pairs
            in the keyword argument list.  For example:  NamespaceDict(one=1, two=2)
        """
        if seq is None:
            super().__init__(**kwargs)
        else:
            super().__init__(seq, **kwargs)

    def __setattr__(self, k: str, v: Any):
        if isinstance(v, dict) and not isinstance(v, NamespaceDict):
            v = NamespaceDict(v)
        self[k] = v

    def __getattr__(self, k: str):
        if k.startswith("_"):
            return super().__getattribute__(k)
        return self[k]

    def __copy__(self):
        return NamespaceDict(self.copy())

    def __deepcopy__(self, memodict=None):
        if memodict is None:
            memodict = {}
        return NamespaceDict(copy.deepcopy(self.copy(), memodict))


def __change_case(data, attr, preserve_dict_class=False):
    """
    Calls data.attr() if data has an attribute/method called attr.
    Processes data recursively if data is a Mapping or Sequence.
    For Mapping, processes both keys and values.
    """
    try:
        return getattr(data, attr)()
    except AttributeError:
        pass

    data_type = data.__class__

    if isinstance(data, Mapping):
        return (data_type if preserve_dict_class else dict)(
            (
                __change_case(key, attr, preserve_dict_class),
                __change_case(val, attr, preserve_dict_class),
            )
            for key, val in data.items()
        )
    if isinstance(data, Sequence):
        return data_type(
            __change_case(item, attr, preserve_dict_class) for item in data
        )
    return data


def _remove_circular_refs(ob, _seen: Set = None):
    """
    Generic method to remove circular references from objects.
    This has been taken from author Martijn Pieters
    https://stackoverflow.com/questions/44777369/
    remove-circular-references-in-dicts-lists-tuples/44777477#44777477
    :param ob: dict, list, typle, set, and frozenset
        Standard python object
    :param object _seen:
        Object that has circular reference
    :returns:
        Cleaned Python object
    """
    if _seen is None:
        _seen = set()
    if id(ob) in _seen:
        # Here we caught a circular reference.
        # Alert user and cleanup to continue.
        log.exception(
            "Caught a circular reference in data structure below."
            "Cleaning and continuing execution.\n%r\n",
            ob,
        )
        return None
    _seen.add(id(ob))
    res = ob
    if isinstance(ob, dict):
        res = {
            _remove_circular_refs(k, _seen): _remove_circular_refs(v, _seen)
            for k, v in ob.items()
        }
    elif isinstance(ob, (list, tuple, set, frozenset)):
        res = type(ob)(_remove_circular_refs(v, _seen) for v in ob)
    # remove id again; only *nested* references count
    _seen.remove(id(ob))
    return res


def compare_dicts(old: Dict = None, new: Dict = None) -> Dict[str, Dict]:
    """
    Compare before and after results from various salt functions, returning a
    dict describing the changes that were made.
    """
    ret = {}
    for key in set((new or {})).union((old or {})):
        if key not in old:
            # New key
            ret[key] = {"old": "", "new": new[key]}
        elif key not in new:
            # Key removed
            ret[key] = {"new": "", "old": old[key]}
        elif new[key] != old[key]:
            # Key modified
            ret[key] = {"old": old[key], "new": new[key]}
    return ret


def object_to_dict(obj) -> Dict:
    """
    Convert an object to a dictionary
    """
    if isinstance(obj, list) or isinstance(obj, tuple):
        ret = []
        for item in obj:
            ret.append(object_to_dict(item))
    elif hasattr(obj, "__dict__"):
        ret = {}
        for item in obj.__dict__:
            if item.startswith("_"):
                continue
            ret[item] = object_to_dict(obj.__dict__[item])
    else:
        ret = obj
    return ret


def is_dictlist(data: List) -> bool:
    """
    Returns True if data is a list of one-element dicts (as found in many SLS
    schemas), otherwise returns False
    """
    if isinstance(data, list):
        for element in data:
            if isinstance(element, dict):
                if len(element) != 1:
                    return False
            else:
                return False
        return True
    return False


def recursive_diff(
    old: Iterable,
    new: Iterable,
    ignore_keys: List = None,
    ignore_order: bool = False,
    ignore_missing_keys: bool = False,
) -> Dict[str, Iterable]:
    """
    Performs a recursive diff on mappings and/or iterables and returns the result
    in a {'old': values, 'new': values}-style.
    Compares dicts and sets unordered (obviously), OrderedDicts and Lists ordered
    (but only if both ``old`` and ``new`` are of the same type),
    all other Mapping types unordered, and all other iterables ordered.

    :param old: Mapping or Iterable to compare from.
    :param new: Mapping or Iterable to compare to.
    :param ignore_keys: List of keys to ignore when comparing Mappings.
    :param ignore_order: Compare ordered mapping/iterables as if they were unordered.
    :param ignore_missing_keys: Do not return keys only present in ``old``
        but missing in ``new``. Only works for regular dicts.
    :return dict: Returns dict with keys 'old' and 'new' containing the differences.
    """
    ignore_keys = ignore_keys or []
    ret_old = copy.deepcopy(old)
    ret_new = copy.deepcopy(new)
    if isinstance(old, Mapping) and isinstance(new, Mapping) and not ignore_order:
        append_old, append_new = [], []
        if len(old) != len(new):
            min_length = min(len(old), len(new))
            # The list coercion is required for Py3
            append_old = list(old.keys())[min_length:]
            append_new = list(new.keys())[min_length:]
        # Compare ordered
        for (key_old, key_new) in zip(old, new):
            if key_old == key_new:
                if key_old in ignore_keys:
                    del ret_old[key_old]
                    del ret_new[key_new]
                else:
                    res = recursive_diff(
                        old[key_old],
                        new[key_new],
                        ignore_keys=ignore_keys,
                        ignore_order=ignore_order,
                        ignore_missing_keys=ignore_missing_keys,
                    )
                    if not res:  # Equal
                        del ret_old[key_old]
                        del ret_new[key_new]
                    else:
                        ret_old[key_old] = res["old"]
                        ret_new[key_new] = res["new"]
            else:
                if key_old in ignore_keys:
                    del ret_old[key_old]
                if key_new in ignore_keys:
                    del ret_new[key_new]
        # If the OrderedDicts were of inequal length, add the remaining key/values.
        for item in append_old:
            ret_old[item] = old[item]
        for item in append_new:
            ret_new[item] = new[item]
        ret = {"old": ret_old, "new": ret_new} if ret_old or ret_new else {}
    elif isinstance(old, Mapping) and isinstance(new, Mapping):
        # Compare unordered
        for key in set(list(old) + list(new)):
            if key in ignore_keys:
                del ret_old[key]
                del ret_new[key]
            elif key in old and key in new:
                res = recursive_diff(
                    old[key],
                    new[key],
                    ignore_keys=ignore_keys,
                    ignore_order=ignore_order,
                    ignore_missing_keys=ignore_missing_keys,
                )
                if not res:  # Equal
                    del ret_old[key]
                    del ret_new[key]
                else:
                    ret_old[key] = res["old"]
                    ret_new[key] = res["new"]
            elif ignore_missing_keys and key in old:
                del ret_old[key]
        ret = {"old": ret_old, "new": ret_new} if ret_old or ret_new else {}
    elif isinstance(old, set) and isinstance(new, set):
        ret = {"old": old - new, "new": new - old} if old - new or new - old else {}
    elif (
        isinstance(old, Iterable)
        and not isinstance(old, str)
        and isinstance(new, Iterable)
        and not isinstance(new, str)
    ):
        # Create a list so we can edit on an index-basis.
        list_old = list(ret_old)
        list_new = list(ret_new)
        if ignore_order:
            for item_old in old:
                for item_new in new:
                    res = recursive_diff(
                        item_old,
                        item_new,
                        ignore_keys=ignore_keys,
                        ignore_order=ignore_order,
                        ignore_missing_keys=ignore_missing_keys,
                    )
                    if not res:
                        list_old.remove(item_old)
                        list_new.remove(item_new)
                        continue
        else:
            remove_indices = []
            for index, (iter_old, iter_new) in enumerate(zip(old, new)):
                res = recursive_diff(
                    iter_old,
                    iter_new,
                    ignore_keys=ignore_keys,
                    ignore_order=ignore_order,
                    ignore_missing_keys=ignore_missing_keys,
                )
                if not res:  # Equal
                    remove_indices.append(index)
                else:
                    list_old[index] = res["old"]
                    list_new[index] = res["new"]
            for index in reversed(remove_indices):
                list_old.pop(index)
                list_new.pop(index)
        # Instantiate a new whatever-it-was using the list as iterable source.
        # This may not be the most optimized in way of speed and memory usage,
        # but it will work for all iterable types.
        ret = (
            {"old": type(old)(list_old), "new": type(new)(list_new)}
            if list_old or list_new
            else {}
        )
    else:
        ret = {} if old == new else {"old": ret_old, "new": ret_new}
    return ret


def repack_dictlist(data, strict=False, recurse=False, key_cb=None, val_cb=None):
    """
    Takes a list of one-element dicts (as found in many SLS schemas) and
    repacks into a single dictionary.
    """
    if isinstance(data, str):
        try:
            data = yaml.safe_load(data)
        except yaml.parser.ParserError as err:
            log.error(err)
            return {}

    if key_cb is None:
        key_cb = lambda x: x
    if val_cb is None:
        val_cb = lambda x, y: y

    valid_non_dict = (str, int, float)
    if isinstance(data, list):
        for element in data:
            if isinstance(element, valid_non_dict):
                continue
            if isinstance(element, dict):
                if len(element) != 1:
                    log.error(
                        "Invalid input for repack_dictlist: key/value pairs "
                        "must contain only one element (data passed: %s).",
                        element,
                    )
                    return {}
            else:
                log.error(
                    "Invalid input for repack_dictlist: element %s is "
                    "not a string/dict/numeric value",
                    element,
                )
                return {}
    else:
        log.error(
            "Invalid input for repack_dictlist, data passed is not a list " "(%s)", data
        )
        return {}

    ret = {}
    for element in data:
        if isinstance(element, valid_non_dict):
            ret[key_cb(element)] = None
        else:
            key = next(iter(element))
            val = element[key]
            if is_dictlist(val):
                if recurse:
                    ret[key_cb(key)] = repack_dictlist(val, recurse=recurse)
                elif strict:
                    log.error(
                        "Invalid input for repack_dictlist: nested dictlist "
                        "found, but recurse is set to False"
                    )
                    return {}
                else:
                    ret[key_cb(key)] = val_cb(key, val)
            else:
                ret[key_cb(key)] = val_cb(key, val)
    return ret


def subdict_match(
    data: Dict,
    expr: str,
    delimiter: str = DEFAULT_TARGET_DELIM,
    regex_match: bool = False,
    exact_match: bool = False,
) -> bool:
    """
    Check for a match in a dictionary using a delimiter character to denote
    levels of subdicts, and also allowing the delimiter character to be
    matched. Thus, 'foo:bar:baz' will match data['foo'] == 'bar:baz' and
    data['foo']['bar'] == 'baz'. The latter would take priority over the
    former, as more deeply-nested matches are tried first.
    """

    def _match(target, pattern):
        target = str(target).lower()
        pattern = str(pattern).lower()

        if regex_match:
            try:
                return re.match(pattern, target)
            except Exception:  # pylint: disable=broad-except
                log.error("Invalid regex '%s' in match", pattern)
                return False
        else:
            return (
                target == pattern if exact_match else fnmatch.fnmatch(target, pattern)
            )

    def _dict_match(target, pattern):
        ret = False
        wildcard = pattern.startswith("*:")
        if wildcard:
            pattern = pattern[2:]

        if pattern == "*":
            # We are just checking that the key exists
            ret = True
        if not ret and pattern in target:
            # We might want to search for a key
            ret = True
        if not ret and subdict_match(
            target, pattern, regex_match=regex_match, exact_match=exact_match
        ):
            ret = True
        if not ret and wildcard:
            for key in target:
                if isinstance(target[key], dict):
                    if _dict_match(target[key], pattern,):
                        return True
                elif isinstance(target[key], list):
                    for item in target[key]:
                        if _match(item, pattern,):
                            return True
                elif _match(target[key], pattern,):
                    return True
        return ret

    splits = expr.split(delimiter)
    num_splits = len(splits)
    if num_splits == 1:
        # Delimiter not present, this can't possibly be a match
        return False

    # If we have 4 splits, then we have three delimiters. Thus, the indexes we
    # want to use are 3, 2, and 1, in that order.
    for idx in range(num_splits - 1, 0, -1):
        key = delimiter.join(splits[:idx])
        if key == "*":
            # We are matching on everything under the top level, so we need to
            # treat the match as the entire data being passed in
            matchstr = expr
            match = data
        else:
            matchstr = delimiter.join(splits[idx:])
            match = traverse_dict_and_list(data, key, {}, delimiter=delimiter)
        log.debug(
            "Attempting to match '%s' in '%s' using delimiter '%s'",
            matchstr,
            key,
            delimiter,
        )
        if match == {}:
            continue
        if isinstance(match, dict):
            if _dict_match(match, matchstr):
                return True
            continue
        if isinstance(match, (list, tuple)):
            # We are matching a single component to a single list member
            for member in match:
                if isinstance(member, dict):
                    if _dict_match(member, matchstr,):
                        return True
                if _match(member, matchstr):
                    return True
            continue
        if _match(match, matchstr):
            return True
    return False


def to_lowercase(data, preserve_dict_class=False):
    """
    Recursively changes everything in data to lowercase.
    """
    return __change_case(data, "lower", preserve_dict_class)


def to_uppercase(data, preserve_dict_class=False):
    """
    Recursively changes everything in data to uppercase.
    """
    return __change_case(data, "upper", preserve_dict_class)


def traverse_dict(
    data: Dict, key: str, default: Any = None, delimiter: str = DEFAULT_TARGET_DELIM
):
    """
    Traverse a dict using a colon-delimited (or otherwise delimited, using the
    'delimiter' param) target string. The target 'foo:bar:baz' will return
    data['foo']['bar']['baz'] if this value exists, and will otherwise return
    the dict in the default argument.
    """
    ptr = data
    try:
        for each in key.split(delimiter):
            ptr = ptr[each]
    except (KeyError, IndexError, TypeError):
        # Encountered a non-indexable value in the middle of traversing
        return default
    return ptr


def traverse_dict_and_list(
    data: Dict or List,
    key: Any,
    default: Any = None,
    delimiter: str = DEFAULT_TARGET_DELIM,
):
    """
    Traverse a dict or list using a colon-delimited (or otherwise delimited,
    using the 'delimiter' param) target string. The target 'foo:bar:0' will
    return data['foo']['bar'][0] if this value exists, and will otherwise
    return the dict in the default argument.
    Function will automatically determine the target type.
    The target 'foo:bar:0' will return data['foo']['bar'][0] if data like
    {'foo':{'bar':['baz']}} , if data like {'foo':{'bar':{'0':'baz'}}}
    then return data['foo']['bar']['0']
    """
    ptr = data
    for each in key.split(delimiter):
        if isinstance(ptr, list):
            try:
                idx = int(each)
            except ValueError:
                embed_match = False
                # Index was not numeric, lets look at any embedded dicts
                for embedded in (x for x in ptr if isinstance(x, dict)):
                    try:
                        ptr = embedded[each]
                        embed_match = True
                        break
                    except KeyError:
                        pass
                if not embed_match:
                    # No embedded dicts matched, return the default
                    return default
            else:
                try:
                    ptr = ptr[idx]
                except IndexError:
                    return default
        else:
            try:
                ptr = ptr[each]
            except KeyError:
                # YAML-load the current key (catches integer/float dict keys)
                try:
                    loaded_key = args.yamlify_arg(each)
                except Exception:  # pylint: disable=broad-except
                    return default
                if loaded_key == each:
                    # After YAML-loading, the desired key is unchanged. This
                    # means that the KeyError caught above is a legitimate
                    # failure to match the desired key. Therefore, return the
                    # default.
                    return default
                else:
                    # YAML-loading the key changed its value, so re-check with
                    # the loaded key. This is how we can match a numeric key
                    # with a string-based expression.
                    try:
                        ptr = ptr[loaded_key]
                    except (KeyError, TypeError):
                        return default
            except TypeError:
                return default
    return ptr
