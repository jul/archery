#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""traits of wits for  Mapping
(any class that quacks like a dict, key like dict, and fly like a dict).
You'll make your code perspire smartness by all its pore(c)(tm)(r).
"""
from numbers import Number
__all__ = [ 'Adder', 'Subber' ]

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
 >>> toto-=( tata+tata )
 >>> print toto
 defaultdict(<type 'int'>, {'a': -1, 'c': 2, 'b': 0})
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
        if isinstance(other,Number):
            self.__iinc__(other)
            return self
            
        for k,v in other.items() :
            self[k] = v+self[k] if k in self else v
        return self
    
    def __radd__(self, other):
        if isinstance(other, Number):
            copy=self.copy()
            return copy.__iinc__(other)
        return self.__add__(other)

