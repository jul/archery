.. _quiver:

Quivers : consistent sets of Traits
===================================

Yes, it is a pun, trait = arrow <=> quiver = set of arrows. 


Available quivers
*****************

VectorDict
----------

A quiver to add cosinus/abs/dot to any MutableMappings
(A mutable mapping is a meta class that behaves like a dict

   >>> from archery.quiver import VectorDict
   >>> from collection import Counter
   >>> from math import cos, pi
   >>> class CCos(Counter, VectorDict): pass
   >>> 
   >>> sim = CCos(["word", "hein?"]).cos(CCos(["word"]))
   >>> assert sim == cos(pi/4)
   >>>
   >>> class Point(VectorDict, cos): pass
   >>> 
   >>> u = Point(x=1, y=1)
   >>> v = Point(x=1, y=0)
   >>> u.cos(v)
   >>> 0.7071067811865475
   >>> u.dot(v)
   >>> 1
   >>> u.cos(2*v)
   >>> 0.7071067811865475
   >>> u.dot(2*v)
   >>> 2
   >>> abs(u)
   >>> 1.4142135623730951




SimplyAdd
---------

A quiver to make your MutableMapping add::

    >>> from archery.quiver import SimplyAdd
    >>> class Daddy(SimplyAdd, dict): pass
    >>>
    >>> a= Daddy({'x' : 1 , 'y' : []}, 'z' : "hell")
    >>> b= Daddy({'x' : 2 , 'y' : [1,3], 'z', "o"})
    >>> print a+b
    # {'y': [1, 3], 'x': 3, 'z': 'hello'}
    >>> a+=b
    >>> print a
    # {'y': [1, 3], 'x': 3, 'z': 'hello'}
    >>>  
    >>> r=Daddy(a=1)
    >>> print r+1
    # {'a': 2}
    >>> print -1+a
    # {'a':0}

If you are smart, you almost have the subtraction ^_^

LinearAlgebrae
--------------

A quiver to make your MutableMapping support + - / * 

Pretty much as easy to use as SimplyAdd






Why quivers?
************

My purpose is not to make trait for the sake of making traits. It is to have 
a bigger set of concrete class for purpose. But I want them to be consistent. 

My (not yet available) unnitest for trait check for actual results (such as 
2+2=4), my unnitest (not yet available) test for how well the operations are 
coupled in terms of commutation, symmetry, distributivity, associativity. 

I see nothing wrong in changing the behviour of add and sub (you may
want to have fun with non euclidian space). But you may want an algebra to
follow the least surprise principle. That's all about it. 



