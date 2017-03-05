#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Traits / mixins are the heart of archery, but sometimes you need functions to help you

"""
from collections import MutableMapping

MARKER=object()
def bowyer(_mapping_fact, _mapping_to_convert):
    """the craftsman that makes bow
    A function that given a function in the form 
    f(tree) will convert a one level tree in your mapping"""
    _toc = _mapping_fact(_mapping_to_convert)
    for k, v in _toc.items():
        if isinstance(v, MutableMapping) and len(v):
            _toc[k] = bowyer(_mapping_fact, v)
    return _toc

def mapping_row_iter(tree, path=MARKER):
    """
    iterator on a tree that yield an iterator on a mapping in the form of 
    a list of ordered key that leads to the element and the value"""
    if path is MARKER:
        path = ()

    for k, v in tree.iteritems():
        if isinstance(v, MutableMapping) and len(v):
            for child in mapping_row_iter(v, (path + (k,))):
                yield child
        else:
            yield path + (k , v)


def paired_row_iter(tree, path=MARKER):
    """
    iterator on a tree that yield a pair key (path to a value), value
    """
    if path is MARKER:
        path = tuple()

    for k, v in tree.iteritems():
        if isinstance(v, MutableMapping) and len(v):
            for child in paired_row_iter(v, path + (k,)):
                yield child
        else:
            yield ((path + (k,)) , v)


