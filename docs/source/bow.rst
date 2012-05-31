.. _bow:

Bow: how not to shoot yourself an arrow in the knee
===================================================

The only reason to use a bow is either you are lazy, or you noticed
I only test these. This is the most tested part of the code yet. 

My philosophy in testing is: check the component relying on the maximum
of your code gives satisfaction since I should traverse most of the point
of failure, and then I add a unittest per bug found. 

Dankyu
******

A dict with addition used here : http://github.com/jul/parseweblog

It instanciate like a dict::
    >>> from archery.bow import Hankyu
    >>> a = Hankyu(x=1,y=2,z=2)

It adds :) ::
    >>> a+a
    {'y': 4, 'x': 2, 'z': 4}
    >>> a+-2
    {'y': 0, 'x': -1, 'z': 0}
    >>> a+.5
    {'y': 2.5, 'x': 1.5, 'z': 2.5}
    >>> .5+a
    {'y': 2.5, 'x': 1.5, 'z': 2.5}

It adds everything consistent with your value::

    >>> a = Hankyu(data=[1,2],sample=1)
    >>> b = Hankyu(data=[3,4],sample=1)
    >>> a+b
    {'sample': 2, 'data': [1, 2, 3, 4]}

If propagates the addition to the included bow::
    >>> a=Hankyu(a=Hankyu(a=1))
    >>> b=Hankyu(a=Hankyu(a=2))
    >>> a+b
    {'a': {'a': 3}}
    >>> a+=1
    >>> a
    {'a': {'a': 2}}
    >>> 

Haikyu
******

A dict that loves to do a lot of things : 
* addition;
* substraction;
* multiplication;
* division (please, please be careful).

Simple algebrae
---------------

It instanciates like a dict:
    >>> from archery.bow import Daikyu
    >>> b=Daikyu(x=2, z=-1)
    >>> a=Daikyu(x=1, y=2.0)
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
    >>> 2*Daikyu(x=1, y="lo",z=[2])
    {'y': 'lolo', 'x': 2, 'z': [2, 2]}
    >>> Daikyu(y=1, z=1)*Daikyu(x=1, y="lo",z=[2])*2
    {'y': 'lolo', 'z': [2, 2]}
    >>> a=Daikyu(dictception=Daikyu(a=1,b=2), sample = 1, data=[1,2])
    >>> b=Daikyu(dictception=Daikyu(c=-1,b=2), sample = 2, data=[-1,-2])
    >>> a+b
    {'sample': 3, 'dictception': {'a': 1, 'c': -1, 'b': 4}, 'data': [1, 2, -1, -2]}
    >>> Daikyu(dictception=1, sample=1)* a*b
    {'sample': 2, 'dictception': {'b': 4}}




