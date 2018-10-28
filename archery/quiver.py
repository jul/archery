#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Soon will come sets of consistent adders/subber/muler/diver
grouped in a consistent set known as algebrae
all the combined traits will ensure consistant properties on :
- commutativity;
- associativity;
- distributivity;
- neutral element of addition & multiplication

Planned : 
Linear algebrae,
Hermitian Algebrae 
and so much more....

"""
from .trait import InclusiveAdder, ExclusiveMuler, Vector
from .trait import InclusiveSubber, TaintedExclusiveDiver
from .trait import Copier


class LinearAlgebrae(
    Copier,
    InclusiveAdder, 
    ExclusiveMuler, 
    TaintedExclusiveDiver, 
    InclusiveSubber):
    """A set of + - * / pretty consistant"""
    pass

class SimplyAdd(Copier, InclusiveAdder): pass

class VectorDict(
        LinearAlgebrae,
        Vector
    ):
    pass


