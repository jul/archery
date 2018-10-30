#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Traits / mixins are the heart of archery, but sometimes you need functions to help you

"""
from collections import MutableMapping

MARKER=object()

class Path(tuple):
    def endswith( self, *a_tuple ):
        """check if path ends with the consecutive given has argumenbts value

 >>> p = Path( [ 'a', 'b', 'c' ] )
 >>> p.endswith( 'b', 'c' )
 >>> True
 >>> p.endswith( 'c', 'b' )
 >>> False
        """
        return self[len(self) - len(a_tuple) : ] == a_tuple

    def startswith( self, *a_tuple ):
        """checks if a path starts with the value

 >>> p = Path( [ 'a', 'b', 'c', 'd' ] )
 >>> p.startswith( 'a', 'b' )
 >>> True
        """
        return self[: len( a_tuple ) ] == a_tuple

    def _contains( self, a_tuple, _from = 0, follow = 0):
        if len( a_tuple) == follow:
            return True
        index = False
        here = self[ _from:]

        try:
            index = here.index(a_tuple[follow] )
            return  self._contains(
                    a_tuple, 
                        index +  1 , 
                        follow + 1
                    )
        except ValueError:
            return False
        return False

    def contains(self, *a_tuple ):
        """checks if the serie of keys is contained in a path

 >>> p = Path( [ 'a', 'b', 'c', 'd' ] )
 >>> p.contains( 'b', 'c' )
 >>> True

        """
        return self._contains(a_tuple)

    def value(self):
        """ function provided for code readability:
        - returns the left most value of the Path aka the value
        """
        return self[-1]

    def key(self):
        """ function provided for code readability:
        - returns all the keys in the Path
        """
        return Path(self[:-1])

def make_from_path(type_of_mapping, path):
    """Work in Progress
    create a mutable mapping from a `Path`_ (tuple made of a series of keys in a dict leading to a
    value followed by a value).
    The source is used a mapping factory and is reset in the process

    >>> make_from_path(dict, ("y", "z", 2))
    >>> #Out[2]: {'y': {'z': 2}}

    """
    path = list(path)
    value = path.pop()
    last_key = path.pop()
    tmap = type_of_mapping
    mapping = tmap({last_key : value})
    while path:
        _next = path.pop()
        mapping = tmap({_next : mapping })
    return mapping

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
    a list of ordered key that leads to the element and the value

    >>> from archery import mapping_row_iter
    >>> [ x for x in mapping_row_iter({
    ...        "john" : {'math':10.0, 'sport':1.0},~
    ...        "lily" : { 'math':20, 'sport':15.0}
    ...    })]
    >>> #[['john', 'sport', 1.0], ['john', 'math', 10.0],~
    >>> #['lily', 'sport', 15.0], ['lily', 'math', 20]]

    """
    if path is MARKER:
        path = ()
    for k, v in tree.items():
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

    for k, v in tree.items():
        if isinstance(v, MutableMapping) and len(v):
            for child in paired_row_iter(v, path + (k,)):
                yield child
        else:
            yield ((path + (k,)) , v)


