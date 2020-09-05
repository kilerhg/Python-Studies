import collections
import collections.abc as abc
import copy
import inspect
import logging
import pop.contract as contract
import pop.hub
import sys
from typing import Any, Dict, Iterable, Iterator, List

log = logging.getLogger(__name__)

__func_alias__ = {
    "immutable_namespaced_map": "imap",
    "mutable_namespaced_map": "map",
    "owner_writeable_namespaced_map": "omap",
}


def immutable_namespaced_map(
    hub: "pop.hub.Hub", init: Dict[str, Any], **kwargs
) -> abc.MutableMapping:
    return IMAP(init_=init, **kwargs)


class IMAP(abc.Mapping):
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
                values[k] = IMAP(init_=v)
            elif isinstance(v, (tuple, int, str, bytes)):
                values[k] = v
            elif isinstance(v, Iterable):
                values[k] = tuple(v)
            else:
                values[k] = v
        # __setattr__ is borked (on purpose) so we have to call it from super() right here
        super().__setattr__("_IMAP__store", values)
        log.debug("Initialized immutable namespaced map")

    def __setattr__(self, k: str, v: Any):
        raise TypeError(
            f"{self.__class__.__name__} does not support attribute assignment"
        )

    def __getattr__(self, k: str):
        if k.startswith("_"):
            return super().__getattribute__(k)
        else:
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
            if isinstance(v, IMAP):
                ret[k] = v.__copy__()
            else:
                ret[k] = v
        return ret

    def __repr__(self):
        return repr(copy.copy(self))


def mutable_namespaced_map(hub: "pop.hub.Hub", dict_: Dict[str, Any] = None) -> "MAP":
    return MAP(dict_=dict_)


class WriteLockError(Exception):
    pass


class MAP(abc.MutableMapping):
    """
    MAP is a key-value store that allows for setting/getting
    by either dot or dictionary lookup notation ('.' or '[k]')

    Sub-keys will be created on assignment:

      `map.foo.bar.baz = True` will auto-create foo and bar as MAPs

    while doing

      `map.foo.bar.baz` before assignment will not create foo, bar or baz.

    :param dict_: similar to dict(dict_), initialize using dict_
    """

    def __init__(self, dict_: Dict[str, Any] = None, parent: "MAP" = None):
        self.__dict__["_store"] = {}
        self.__dict__["_parent"] = parent
        if dict_:
            # Existing dictionaries might have properties that need wrapped as well
            self.update(dict_)

    def _set(self, k: str, v: Any):
        if k.startswith("_"):
            raise AttributeError("Cannot store values beginning with '_'")

        if isinstance(v, dict):
            # Cast all nested dict values as MAP so they get it's benefits as well
            v = self.__class__(dict_=v, parent=self)
            self._store[k] = v
        else:
            self._store[k] = v

    def _get(self, k: str, create: bool = False):
        if k.startswith("_"):
            return super().__getattribute__(k)
        try:
            if k not in self._store:
                if not create:
                    return UninitializedValue([k], self)
                self._set(k, self.__class__())
            return self._store[k]
        except Exception as e:
            raise AttributeError(*e.args)

    def get(self, k: str, default: Any = None) -> Any:
        if k in self._store:
            return getattr(self, k)
        else:
            return default

    def __setitem__(self, k: str, v: Any):
        self._set(k, v)

    def __delitem__(self, k: str):
        """
        Cleanup method required by abc.ABC
        """
        if k in self._store:
            del self._store[k]

    def __delattr__(self, k: str):
        self.__delitem__(k)

    def __getitem__(self, k: str) -> Any:
        return self._get(k)

    def __getattr__(self, k: str) -> Any:
        return self._get(k)

    def __setattr__(self, k: str, v: Any):
        self._set(k, v)

    def __contains__(self, k: str) -> Any:
        return k in self._store

    def __len__(self) -> int:
        return len(self._store)

    def __iter__(self) -> Iterator[Any]:
        return iter(self._store)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({str(self)})"

    def __str__(self) -> str:
        return str(self._store)

    def __copy__(self) -> Dict[str, Any]:
        # The copy will be a dictionary, mangle it all you want
        ret = {}
        for k, v in self._store.items():
            if isinstance(v, MAP):
                ret[k] = v.__copy__()
            else:
                ret[k] = v
        return ret


class UninitializedValueError(Exception):
    pass


class UninitializedValue:
    """
    We want you to be able to create data on the MAP by doing something like:

        MAP.foo.bar = True

    However, we want uses of un-initialized values to blow up, not auto-create.

    We build up a potentially pending write using a special object that can only be written.
    Any other use should blow up.

    """

    def __init__(self, path: List[str], map_: MAP):
        # The path I'm looking up on the map
        self.__dict__["_path"] = path
        self.__dict__["_map"] = map_

    def _blowup(self):
        raise UninitializedValueError(
            f"Access of uninitialized value '{'.'.join(self.__dict__['_path'])}'"
        )

    def __getattribute__(self, item: str):
        if item == "get":
            pass
        elif not item.startswith("_"):  # return a new PendingWrite for regular lookups
            new_path = self._path[:]
            new_path.append(item)
            return UninitializedValue(new_path, self._map)
        elif item not in (
            "__class__",
            "__dict__",
            "__setattr__",
            "_blowup",
            "_map",
            "_path",
            "get",
        ):
            self._blowup()
        return super().__getattribute__(item)

    def __setattr__(self, k: str, v: Any):
        node = self._map
        for part in self._path:
            node = node._get(part, create=True)

        setattr(node, k, v)

    def __delattr__(self, k: str):
        pass

    def __getitem__(self, item: str):
        return getattr(self, item)

    def __setitem__(self, k: str, v: Any):
        setattr(self, k, v)

    def __delitem__(self, k: str):
        pass

    def get(self, k: str, default: Any = None) -> Any:
        return default

    def __bool__(self) -> bool:
        # Uninitialized values always evaluate to false
        return False

    def __contains__(self, item: str) -> bool:
        # If it contained anything it would be initialized
        return False

    def __hash__(self):
        self._blowup()

    def __dir__(self):
        self._blowup()

    def __str__(self):
        self._blowup()


def owner_writeable_namespaced_map(
    hub, dict_: Dict[str, Any] = None
) -> "OwnerWriteableMapping":
    return OwnerWriteableMapping(dict_=dict_)


def _stack_frames(relative_start=2):
    """
    Efficiently access stack frames.
    :param relative_start: Starting stack depth; The default, 2 is the parent of the
                           caller of stack_frames - the first function that may be unknown.
    :return: a stack frame
    """
    if hasattr(sys, "_getframe"):
        # implementation detail of CPython, speeds things up by 100x.
        frame = sys._getframe(relative_start)
        while frame:
            yield frame
            frame = frame.f_back
    else:
        for frame_info in inspect.stack(context=0)[relative_start:]:
            yield frame_info.frame


WriteLockInfo = collections.namedtuple("WriteLockInfo", ["val", "owner", "lineno"])


class OwnerWriteableMapping(MAP):
    """
    A MAP variant that is write-locked to the first Contracted function
    that writes to a given key (becoming the owner). Attempts to write
    to that key from other functions will receive a WriteLockError showing
    the owning Contracted function.
    """

    def __init__(
        self, dict_: Dict[str, Any] = None, parent: "OwnerWriteableMapping" = None
    ):
        super().__init__(dict_, parent)

    def _find_owner(self) -> (contract.Contracted, int):
        """
        Return the contracted responsible for assigning to this variable.
        Returns None if no such function exists.
        """
        for frame in _stack_frames(3):
            if isinstance(frame.f_locals.get("self"), contract.Contracted):
                contracted = frame.f_locals["self"]
                log.debug(f"Found contract '{contracted.__name__}'")
                break
            else:
                # find the lineno in the frame *before* our Contracted (the function called)
                lineno = frame.f_lineno
        else:
            # not found
            contracted = None
            lineno = -1

        return contracted, lineno

    def _set(self, k: str, v: Any):
        owner, lineno = self._find_owner()
        cur = self._store.get(k)
        if cur is None or cur.owner is owner:
            if isinstance(v, abc.Mapping):
                v = self.__class__(dict_=v, parent=self)
            elif isinstance(v, Iterable) and not isinstance(
                v, (tuple, str, bytes, UninitializedValue)
            ):
                v = tuple(v)  # Lists, sets, and other iterables become immutable
            super()._set(k, WriteLockInfo(v, owner, lineno))
        else:
            file = inspect.getsourcefile(cur.owner.func)
            raise WriteLockError(
                f"'{k}' was previously assigned by '{cur.owner.__name__}' ({file}:{cur.lineno})"
            )

    def _get(self, k: str, create: bool = False) -> Any:
        v = super()._get(k, create)
        if not isinstance(v, UninitializedValue):
            v = v.val
        return v

    def __str__(self) -> str:
        return str(self._dict())

    def _dict(self):
        vals = {}
        for k, v in self._store.items():
            if isinstance(v.val, self.__class__):
                vals[k] = v.val._dict()
            else:
                vals[k] = v.val
        return vals
