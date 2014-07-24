#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""traits of wits for  MutableMapping
(any class that quacks like a dict, key like dict, and fly like a dict).
You'll make your code perspire smartness by all its pore(c)(tm)(r).
"""
from __future__ import division
from collections import MutableMapping
from .barrack import mapping_row_iter
__all__ = [ 'InclusiveAdder', 'InclusiveSubber', 
    'ExclusiveMuler', 'TaintedExclusiveDiver', 'Copier', 'Iterator', 'Searchable']

class Funct(funct):
    
class Copier(object):
    def copy(self):
        if hasattr(super(Copier, self),"copy"):
            return self.__class__(super(Copier, self).copy())
        else:
            return [ x for x in self]


class InclusiveAdder(object):
    """ making dict able to add 

 >>> from archery.trait import Adder
 >>> from collections import defaultdict
 >>> class dad(defaultdict,Adder,Subber):pass
 ... 
 >>> tata = dad( int, dict(a = 1, b = 0, c = -1 ) )
 >>> 
 >>> toto = dad( int, dict(a = 1 ) )
 >>> print toto+tata
 defaultdict(<type 'int'>, {'a': 2, 'c': -1, 'b': 0})
 >>> toto+=1
 defaultdict(<type 'int'>, {'a': 2}

"""

    def __add__(self, other):
        """adder"""
        copy = self.copy()
        copy.__iadd__(other)
        return copy

    def __iinc__(self, number):
        """in place increment"""
        for k, v in self.items():
            self[k] += number
        return self

    def __iadd__(self, other):
        if not isinstance(other, MutableMapping):
            self.__iinc__(other)
            return self
        for k, v in other.items():
            if k in self:
                self[k] += v
            else:
                self[k]=v
        return self

    def __radd__(self, other):
        copy = self.copy()
        if not isinstance(other, MutableMapping):
            return copy.__iinc__(other)
        return copy.__iadd__(other)


class TaintedExclusiveDiver(object):
    """Making dict able to truedivide (you need to provide a muler)
    This operator is tainted thanks to my inability to make neither
    from __future__ import truedivision
    nor
    from operator import truetruediv
    works. 
    So as a result I use implicit 1.0 cast
    
    Why don't I stick to regular (broken) python truedivision ? 
    Don't you think this  : 
    0.5 * a == a / 2
    less surprising than :
    a/2 = something that is part /2 (if result is int),
    and sometimes something else

    )"""
    def __div__(self,other):
        return self.__truediv__(other)

    def __idiv__(self,other):
        return self.__itruediv__(other)

    def __rdiv__(self,other):
        return self.__rtruediv__(other)

    def __truediv__(self, other):
        """truediver"""
        copy = self.copy()
        if not isinstance(other, MutableMapping):
            return copy.__iscalmul__(1 / other)
        copy /= other
        return copy

    def __itruediv__(self, other):
        if not isinstance(other, MutableMapping):
            self.__iscalmul__(1 / other)
            return self
        todel=[]
        for k in self:
            if k in other:
                self[k] /=  other[k]
            else:
                todel +=[k]
        for k in todel: del(self[k])
        return self
   

    def __iinv__(self):
        """in place inversion 1/a"""
        for k,v  in self.items():
            self[k] =1/v 
        return self

    def __rtruediv__(self, other):
        copy = self.copy()
        if not isinstance(other, MutableMapping):
            return copy.__iinv__().__iscalmul__(other)
        return copy / other


class ExclusiveMuler(object):
    """Making dict able to multiply"""

    def __mul__(self, other):
        """muler"""
        copy = self.copy()
        copy *= other
        return copy

    def __iscalmul__(self, number):
        """in place increment"""
        for k,v in self.items():
            self[k] *= number
        return self

    def __imul__(self, other):
        if not isinstance(other, MutableMapping):
            self.__iscalmul__(other)
            return self
        todel=[]
        for k in self:
            if k in other:
                self[k] *= other[k] 
            else:
                todel+=[k]
        for k in todel: del(self[k])
        return self

    def __rmul__(self, other):
        copy = self.copy()
        if not isinstance(other, MutableMapping):
            return copy.__iscalmul__(other)
        return copy.__mul__(other)

class Iterator(object):

    def __iter__(self):
        self.__iter = mapping_row_iter(self)
        return self.__iter

    def __next__(self):
        return self.__iter()

class InclusiveSubber(object):
    def __sub__(self, other):
        """suber"""
        copy = self.copy()
        copy -= other
        return copy

    def __isub__(self, other):
        if not isinstance(other, MutableMapping):
            self.__iinc__(-other)
            return self
        for k,v in other.items():
            self[k] = self[k] - v if k in self else -v
        return self

    def __rsub__(self, other):
        copy = self.copy()
        if not isinstance(other, MutableMapping):
            return copy.__neg__().__iinc__(other)
        return copy.__sub__(other)

    def __neg__(self):
        """in place negation"""
        for k,v in self.items():
            self[k] *= -1
        return self

_mark = object()
class Searchable(Iterator):

    def gu_rsearch(self, pred, tr=_mark):
        """greedy unsafe recursive search
        return a tuple of type path to value when predicate is match

        lazy and unsafe because it is note the right way to do it
        but lazy because it works fine.
        for an element. """
        if tr is _mark:
           tr=()
        if pred(self):
            yield tr, self
        for k, v in self.items():
            if hasattr(v, "gu_rsearch"):
                for res in v.gu_rsearch(pred, tr + (k,)):
                    if res: yield res


    def lu_rsearch(self, pred, tr=_mark):
        """lazy unsafe recursive search
        return a tuple of type path to value when predicate is match

        lazy and unsafe because it is note the right way to do it
        but lazy because it works fine.
        for an element. """
        if tr is _mark:
           tr=()
        if pred(self):
            yield tr, self
        else:
            for k, v in self.items():
                if hasattr(v, "lu_rsearch"):
                    for res in v.lu_rsearch(pred, tr + (k,)):
                        if res: yield res

    def search(self, predicate):
        for el in self:
            if predicate(el):
                yield el

    def leaf_search(self, predicate_on_leaf):
        for el in self:
            path, value = el
            if predicate_on_leaf(value):
                yield value

    def propagate(self, pred, funct_true, funct_false):
        for k, v in self.items():
            if pred(v):
                self[k] = funct_true(v)
            else:
                self[k] = funct_false(v)
            if hasattr(self[k], "propagate"):
                self[k].propagate(pred, funct_true, funct_false)

    def incr_p(self,x):
        can_add = lambda n: hasattr(n, "__add__")
        self.propagate(can_add, lambda n: n+x, lambda x:x)

    def bless(self, _type):
        do_nothing = lambda x : x
        def convert(node):
            return _type(node)
        def has_type(node):
            return isinstance(node, MutableMapping
                ) and not isinstance(node,_type)
        self.propagate(has_type, convert, do_nothing)

