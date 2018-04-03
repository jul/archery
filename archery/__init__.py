#!/usr/bin/env python
# -*- coding: utf8 -*-
"""Making dict great vectors!


"""

from .bow import Daikyu as mdict
from .barrack import paired_row_iter
__version__ = "0.1.7"
__all__ = [
    "__version__", "dot", "abs", "cos", "mdict", "paired_row_iter" ]


def dot(u, v):
    """
    scalar product of two MappableMappings (recursive)
    """
    return sum(v for i,v in paired_row_iter(u*v))


def abs(v):
    """return the absolute value (hence >=0)
    aka the distance from origin
    """
    return dot(v, v)**.5

def cos(u, v):
    """Thought the cos({}, any) yielding a divided / 0 exc was a bug
    It's totally okay
    http://math.stackexchange.com/a/932454
    only works for orthonormalised space, use jaccard else.
    """
    return dot(u, v) / abs(u) / abs(v)



