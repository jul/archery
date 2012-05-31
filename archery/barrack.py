#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Traits / mixins are the heart of archery, but sometimes you need functions to help you

"""
from collections import Mapping

def bowyer(_mapping_fact, _mapping_to_convert):
    """the craftsman that makes bow
    A function that given a function in the form 
    f(tree) will convert a one level tree in your mapping"""
    _toc = _mapping_fact(_mapping_to_convert)
    for k, v in _toc.iteritems():
        if isinstance(v, Mapping):
            _toc[k] = bowyer(_mapping_fact, v)
    return _toc

def mapping_row_iter(tree, path=None):
    """
    iterator on a tree that yield an iterator on a mapping in the form of 
    a list of ordered key that leads to the element and the value"""
    if path is None: path = []

    for k, v in tree.iteritems():
        if isinstance(v, Mapping):
            for child in mapping_row_iter(v, (path + [k])):
                yield child
        else:
            yield path + [k , v]
