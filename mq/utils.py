#!/usr/bin/env python
# coding: utf-8

"""
Utilities
"""

from collections import OrderedDict, Mapping, MutableMapping, Iterable
import threading


class Enum(Mapping):
    """
    Readonly enumeration.
    e.g. ::
    my_enum = Enum(a=1, b=2)
    my_enum = Enum({
            a: 1,
            "B": "two",
            })
    my_enum = Enum([
            (a, 1),
            ("b", "two),
            ])
    my_enum.a = 1
    my_enum['b'] = "two"
    ::
    """

    def __init__(self, iterable=None, **kwargs):
        super(Enum, self).__init__()
        self._enums = OrderedDict()
        self._lock = threading.RLock()
        self._update(iterable, **kwargs)

    def _update(self, iterable=None, **kwargs):
        if iterable is not None:
            if isinstance(iterable, Mapping):
                items = iterable.items()
            elif isinstance(iterable, Iterable):
                items = iterable
            else:
                raise TypeError('%s is not Iterable' % str(iterable))

            for k, v in items:
                with self._lock:
                    self._enums[k] = v
                    setattr(self, k, v)
        for k, v in kwargs.items():
            with self._lock:
                self._enums[k] = v
                setattr(self, k, v)

    def __len__(self):
        return len(self._enums)

    def __getitem__(self, key):
        return self._enums[key]

    def __iter__(self):
        for key in self._enums:
            yield (key, self._enums[key])


class MutableEnum(Enum, MutableMapping):
    """
    Mutable enumeration. Inherits from Enum.
    """

    def __setitem__(self, key, value):
        with self._lock:
            self._enums[key] = value
            setattr(self, key, value)

    def __delitem__(self, key):
        with self._lock:
            del self._enums[key]
            delattr(self, key)

    def pop(self, key, default=None):
        with self._lock:
            value = self._enums.pop(key)
            delattr(self, key)
            return value

    def popitem(self):
        with self._lock:
            k, v = self._enums.popitem()
            if k:
                delattr(self, k)
            return v

    def clear(self):
        with self._lock:
            for k in self._enums.keys():
                delattr(self, k)
            self._enums.clear()

    def update(self, iterable=None, **kwargs):
        self._update(iterable, **kwargs)