#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""traits of wits for  Mapping
(any class that quacks like a dict, key like dict, and fly like a dict).
You'll make your code perspire smartness by all its pore(c)(tm)(r).
"""
from collections import Mapping
from numbers import Number
__all__ = [ 'Adder', 'Subber', 'Muler', 'Diver' ]

class Adder():
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
        copy += other
        return copy

    def __iinc__(self,number):
        """in place increment"""
        for k,v in self.iteritems():
            self[k] += number
        return self
        
    def __iadd__(self, other):
        if not isinstance(other,Mapping):
            self.__iinc__(other)
            return self
            
        for k,v in other.items() :
            self[k] = v+self[k] if k in self else v
        return self
    
    def __radd__(self, other):
        copy=self.copy()
        if not isinstance(other, Mapping):
            return copy.__iinc__(other)
        return copy.__iadd__(other)


class Diver():
    """Making dict able to divide (you need to provide a muler)"""

    def __div__(self, other):
        """diver"""
        copy = self.copy()
        copy /= other
        return copy

    def __idiv__(self, other):
        if isinstance(other,Number):
            self.__iscalmul__(1.0 / other)
            return self
        for k in other:
            if k  in self:
                self[k] /= 1.0 *  other
        return self
    
    def __rdiv__(self, other):
        if isinstance(other, Number):
            copy=self.copy()
            return copy.__iscalmul__(1.0/other)
        return self.__div__(other)

class Muler():
    """Making dict able to multiply"""

    def __mul__(self, other):
        """muler"""
        copy = self.copy()
        copy *= other
        return copy

    def __iscalmul__(self,number):
        """in place increment"""
        for k,v in self.iteritems():
            self[k] *= number
        return self
        
    def __imul__(self, other):
        if isinstance(other,Number):
            self.__iscalmul__(other)
            return self
        for k in other:
            if k  in self:
                self[k] = other[k]*self[k]
        return self
    
    def __rmul__(self, other):
        if isinstance(other, Number):
            copy=self.copy()
            return copy.__iscalmul__(other)
        return self.__mul__(other)

class Subber():
    def __sub__(self, other):
        """suber"""
        copy = self.copy()
        copy -= other
        return copy

    def __isub__(self, other):
        if not isinstance(other,Mapping):
            self.__iinc__(-other)
            return self
        for k,v in other.items() :
            self[k] = self[k]-v  if k in self else -v
        return self
    
    def __rsub__(self, other):
        if not isinstance(other,Mapping):
            copy=self.copy()
            return copy.__iinc__(-other)
        return self.__sub__(other)
    
    def __neg__(self):
        for k,v in self.iteritems():
            self[k]*=-1
        return self
