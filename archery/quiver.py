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
from .trait import Adder, Muler, Subber, Diver

class LinearAlgebrae(Adder, Muler, Diver, Subber):
    """A set of + - * / pretty consistant"""
    pass

