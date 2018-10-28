.. _bow:

Bow Specialized dict ready to use based on quivers
==================================================

vdict
-----

A dict that supports cosine, abs, dot product::

   >>> from archery import vdict as Point
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
   >>> u3 = Point(x=1, y=1, z=2)
   >>> u4 = Point(x=1, y=3, z=4)
   >>> u3 + u4
   >>> dict(x=2, y=4, z=6)
   >>> assert u4 + u4 == 2*u4
   

mdict (former Daikyu)
---------------------

Mnemonic for multiplicative dict that can

* addition;
* substraction;
* multiplication;
* division (please, please be careful).

It instanciates like a dict:
    >>> from archery import mdict
    >>> b=mdict(x=2, z=-1)
    >>> a=mdict(x=1, y=2.0)
    >>> a+b
    # OUT: {'y': 2.0, 'x': 3, 'z': -1}
    >>> b-a
    # OUT: {'y': -2.0, 'x': 1, 'z': -1}
    >>> -(a-b)
    # OUT: {'y': -2.0, 'x': 1, 'z': -1}
    >>> a+1
    # OUT: {'y': 3.0, 'x': 2}
    >>> -1-a
    >>> # OUT: {'y': -3.0, 'x': -2}
    >>> a*b
    # OUT: {'x': 2}
    >>> a/b
    # OUT: {'x': 0}
    >>> 1.0*a/b
    # OUT: {'x': 0.5}

Why div is special?
-------------------

Because div is special and I stick to python 2 behaviour on this one.

http://beauty-of-imagination.blogspot.fr/2012/05/dividing-is-not-as-easy-at-it-seems.html

Don't flame me yet, I can provide another diver, but my brain is yet kaput. 

See by yourself::
    >>> b/2
    # OUT: {'x': 0, 'z': 0}
    >>> b/2.0
    # OUT: {'x': 1.0, 'z': -0.5}
    >>> 2/b
    # OUT: {'x': 0, 'z': -2}

But you can correct this::
    >>> 2.0/(1.0*b)
    # OUT: {'x': 1.0, 'z': -2.0}


Mixing scalars and records
--------------------------

My prefered part :) ::

    >>> 2*mdict(x=1, y="lo",z=[2])
    {'y': 'lolo', 'x': 2, 'z': [2, 2]}
    >>> mdict(y=1, z=1)*Daikyu(x=1, y="lo",z=[2])*2
    {'y': 'lolo', 'z': [2, 2]}
    >>> a=mdict(dictception=dict(a=1,b=2), sample = 1, data=[1,2])
    >>> b=mdict(dictception=dict(c=-1,b=2), sample = 2, data=[-1,-2])
    >>> a+b
    {'sample': 3, 'dictception': {'a': 1, 'c': -1, 'b': 4}, 'data': [1, 2, -1, -2]}
    >>> mdict(dictception=1, sample=1)* a*b
    {'sample': 2, 'dictception': {'b': 4}}

Whatever meanings you gave to + it propagates the meaning.
For algebraic use I recommend to use algebraic types (complex, numpy arrays,
floats, int).



