.. _barrack:

Barrack: the place for stuff connected to archery
=================================================

bowyer
******

Lazyness facility for converting a tree of a MutableMappping type in another one::
    >>> from archery.barrack import bowyer
    >>> from archery.bow import Daikyu
    >>> a=bowyer(Daikyu,{'a':{'b':{'c' : [ 1, 2 ] }}, 'c' : 3.3})
    >>> a*2
    {'a': {'b': {'c': [1, 2, 1, 2]}}, 'c': 6.6}

It works also with lambda a_tree:defaultdict(int,a_tree) instead od Daikyu::

mapping_row_iter
****************

My secret weapon for transforming dict in CSV::

   >>> from archery.barrack import mapping_row_iter
   >>> [ x for x in mapping_row_iter({
   ...     "john" : {'math':10.0, 'sport':1.0}, 
   ...     "lily" : { 'math':20, 'sport':15.0}
   ... })]
   [['john', 'sport', 1.0], ['john', 'math', 10.0], 
   ['lily', 'sport', 15.0], ['lily', 'math', 20]]

