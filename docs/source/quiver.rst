.. _quiver:

Quivers : consistent sets of Traits
===================================

Yes, it is a pun, trait = arrow <=> quiver = set of arrows. 


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

Available quivers
*****************

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






