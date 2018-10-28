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
__all__ = [ 'Hankyu', 'Daikyu', "edict", 'mdict' ]

from .trait import (
        InclusiveAdder, InclusiveSubber, ExclusiveMuler, 
        Iterator, Searchable 
    )
from .quiver import LinearAlgebrae, VectorDict
from .barrack import bowyer
from collections import MutableMapping


class RecIniter(object):
    
    def __init__(self, *a, **kw):
        my_class = locals().get(type(self).__name__,
                            globals()[type(self).__name__])
        getattr(my_class,"mapping").__init__(self, *a, **kw)
        for k, v in self.items():
            if not isinstance(v, my_class) and isinstance(v, MutableMapping):
                self[k] = bowyer(my_class , v)


class _Hankyu(InclusiveAdder,dict):
    pass



class Hankyu(InclusiveAdder, RecIniter):
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
    mapping = dict

class Hankyu(_Hankyu, dict):
    """Fix the broken copier
    metaclass are hard"""
    def copy(self):
        return bowyer(Hankyu, self)


class _Daikyu(LinearAlgebrae, RecIniter):
    """japanese longbow"""
    mapping = dict

class Daikyu(_Daikyu, dict):
    """Fix the broken copier
    metaclass are hard"""
    def copy(self):
        return bowyer(Daikyu, self)

mdict = Daikyu



class vdict(RecIniter, VectorDict, dict):
    mapping = dict

class _sdict(Searchable, LinearAlgebrae, RecIniter, dict):
    """japanese longbow"""
    mapping = dict

class sdict(_sdict):
    pass


### for compatibility puprose
class edict(_sdict):

    def __init__(self, *a, **kw):
        super(_sdict, self).__init__(*a, **kw)
        warns("ExpDict/edict will become sdict", DeprecationWarning)
        for k, v in self.items():
            if isinstance(v, MutableMapping):
                self[k] = bowyer(globals()[type(self).__name__], v)


