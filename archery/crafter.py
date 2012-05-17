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
from collections import Mapping

def bowyer(_mapping_fact, _mapping_to_convert):
    _toc = _mapping_fact(_mapping_to_convert)
    for k,v in _toc.iteritems():
        if isinstance(v,Mapping):
            _toc[k] = encoche( _mapping_fact, v)
    return _toc

def fletcher(tree, path=list()):
    for k,v in tree.iteritems():
        if isinstance(v,Mapping):
            for child in fletcher(v, (path + [ k ]) ):
                yield child

        else:
            yield   path + [k ,  v ] 
    
