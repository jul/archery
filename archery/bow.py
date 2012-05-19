#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
All you need to shoot yourself an arrow in the knee : preconfigured class
that seems harmless and seems to be powerfull. 

"""
__all__ = [ 'Daddy', 'DDWA']

from .trait import Adder
from .quiver import LinearAlgebrae
from collections import defaultdict

class ShortBow(Adder, defaultdict):
    """Use this at your own risk.
    DDWA is the sigle for d(efault)dict with addition
    Daddy is the same class with the mnemonic for d(efault)dict with addition

 >>> from archery.weapon import  Daddy 
 >>> tata = Daddy( int, dict(a = 1, b = 0, c = -1 ) )
 >>> 
 >>> toto = Daddy( int, dict(a = 1 ) )
 >>> print toto+tata
 defaultdict(<type 'int'>, {'a': 2, 'c': -1, 'b': 0})
 >>> toto-=( tata+tata )
 >>> print toto
 defaultdict(<type 'int'>, {'a': -1, 'c': 2, 'b': 0})
"""
    pass


class Daikyu(LinearAlgebrae, defaultdict):
    """japanese longbow"""
    pass


class LongBow():
    def __init__(self):
        raise Exception("This class is reserved for my prefered one")
