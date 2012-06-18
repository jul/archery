#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""traits of wits for  MutableMapping
(any class that quacks like a dict, key like dict, and fly like a dict).
You'll make your code perspire smartness by all its pore(c)(tm)(r).
"""
#from __future__ import division
from collections import MutableMapping
__all__ = [ 'InclusiveAdder', 'InclusiveSubber', 
    'ExclusiveMuler', 'TaintedExclusiveDiver', 'Copier', "IterItemsEmulator"]

class Copier(object):
    def copy(self): 
        if hasattr(super(Copier, self),"copy"):
            return self.__class__(super(Copier, self).copy())
        else:
            return [ x for x in self]

class IterItemsEmulator(object):
    def iteritems(self):
        for i in self:
            yield i

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
        for k, v in self.iteritems():
            self[k] += number
        return self

    def __iadd__(self, other):
        if not isinstance(other, MutableMapping):
            self.__iinc__(other)
            return self
        for k, v in other.items():
            if k in self;
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
    """Making dict able to divide (you need to provide a muler)
    This operator is tainted thanks to my inability to make neither
    from __future__ import division
    nor
    from operator import truediv
    works. 
    So as a result I use implicit 1.0 cast
    
    Why don't I stick to regular (broken) python division ? 
    Don't you think this  : 
    0.5 * a == a / 2
    less surprising than :
    a/2 = something that is part /2 (if result is int),
    and sometimes something else

    )"""


    def __div__(self, other):
        """diver"""
        copy = self.copy()
        if not isinstance(other, MutableMapping):
            return copy.__iscalmul__(1 / other)
        copy /= other
        return copy

    def __idiv__(self, other):
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
        for k,v  in self.iteritems():
            self[k] =1/v 
        return self
        
    def __rdiv__(self, other):
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
        for k,v in self.iteritems():
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
        for k,v in self.iteritems():
            self[k] *= -1
        return self
