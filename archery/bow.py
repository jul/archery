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
__all__ = [ 'Hankyu', 'Daikyu', "vdict","sdict", 'mdict' ]

from .trait import (
        InclusiveAdder, InclusiveSubber, ExclusiveMuler, 
        Iterator, Searchable 
    )
from .quiver import LinearAlgebrae, VectorDict
from .barrack import bowyer
from collections import MutableMapping
from warnings import warn



class _Hankyu(InclusiveAdder,dict):
    pass


class Hankyu(InclusiveAdder):
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
from copy import deepcopy
class Hankyu(_Hankyu, dict):
    """Fix the broken copier
    metaclass are hard"""
    def copy(self):
        return deepcopy(
            bowyer(
                Hankyu,
                self
            )
        )


class _Daikyu(LinearAlgebrae):
    """japanese longbow"""
    """Fix the broken copier
    metaclass are hard"""
    def copy(self):
        return deepcopy(
            bowyer(
                Daikyu,
                self
            )
        )

class Daikyu(_Daikyu, dict):
    """Fix the broken copier
    metaclass are hard"""
    pass


mdict = Daikyu


class _vdict(VectorDict,dict): pass

class vdict(_vdict):
    def __init__(self, *a, **kw):
        super(_vdict, self).__init__(*a, **kw)
        for k, v in self.items():
            if isinstance(v, MutableMapping):
                self[k] = bowyer(globals()[type(self).__name__], v)

class _sdict(Searchable, LinearAlgebrae, dict):
    """japanese longbow"""
    mapping = dict

class sdict(_sdict):
    pass


### for compatibility puprose
class edict(_sdict):

    def __init__(self, *a, **kw):
        warn("ExpDict/edict will become sdict", DeprecationWarning)
        super(_sdict, self).__init__(*a, **kw)
        for k, v in self.items():
            if isinstance(v, MutableMapping):
                self[k] = bowyer(globals()[type(self).__name__], v)


