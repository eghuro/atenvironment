# -*- coding: utf-8 -*-

"""Main module."""

import os
import logging
from functools import wraps


class UnknownKeyword(BaseException):
    pass


class EnvironMiss(KeyError):
    pass


def _missing(value):
    log = logging.getLogger(__name__)
    log.error("Missing environment variable: %s" % (value))
    raise EnvironMiss(value)


_allowed_keywords = ['onerror']


def environment(*value, **kwargs):
    err = _missing

    if kwargs is not None:
        for k in kwargs:
            if k not in _allowed_keywords:
                raise UnknownKeyword(k)

        if 'onerror' in kwargs:
            err = kwargs['onerror']

    def environ_decorator(func):
        @wraps(func)
        def inner(*args):
            for v in value:
                if v not in os.environ:
                    err(v)
            return func(*args, *[os.environ[v] for v in value])
        return inner
    return environ_decorator
