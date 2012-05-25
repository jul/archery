#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
All you need to shoot yourself an arrow in the knee : preconfigured class
that seems harmless and seems to be powerfull. 

Short bows = one operator 
long bows = one quiver
Cross bow = algebrae + other quiver
Japanese bows : algebrae
European bows (common names) : proposed standard behaviour
I think I am already short of ideas

"""
__all__ = [ 'Hankyu', 'Daikyu' ]

from .trait import InclusiveAdder,Copier, InclusiveSubber,ExclusiveMuler
from .quiver import LinearAlgebrae

class Hankyu(Copier,InclusiveAdder,dict):
    """Use this at your own risk.
    Hankyu is the same class with the mnemonic for d(efault)dict with addition

 >>> from archery.bow import Hankyu
 >>> tata = Hankyu( dict(a = 1, b = 0, c = -1 ) )
 >>> 
 >>> toto = Hankyu( dict(a = 1 ) )
 >>> print toto+tata
 {'a': 2, 'c': -1, 'b': 0}
 >>> toto-=( tata+tata )
 >>> print toto
 {'a': -1, 'c': 2, 'b': 0}
"""
    pass


class Daikyu(LinearAlgebrae, dict): 
    """japanese longbow"""
    pass

class SafeDaikyu(Copier, InclusiveAdder, InclusiveSubber, ExclusiveMuler):
    """Safe Daikyu"""
    pass


class LongBow():
    def __init__(self):
        raise Exception("This class is reserved for my prefered one")


