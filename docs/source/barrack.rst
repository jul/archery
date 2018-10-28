.. _barrack:

Barrack: the place for stuff connected to archery
=================================================

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


