Having fun
==========

Mixing scalars and records (side effect)
****************************************

You can also the use the addition in the meaning of a record.
That is what the yahi module on pypi does https://github.com/jul/yahi ::


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

Pushing the vice to create a rotation matrix with a dict
********************************************************

.. literalinclude:: _static/matrix.py


Design
======

Traits are Mixins, behaviours. All these terms recovers loosely the same idea.

In this case refering to even older conventions traits are concrete classes for abstract classes/interfaces. 

collections.MutableMapping defines an interface and some concrete methods. Since isinstance relies on interfaces (ducktyping) 
I can safely use it to implement methods that don't exists and will normally work for most Mappings. 

.. warning: Traits relies on copy, if ever you define a custom constructor, don't forget the `rule of three`_. 
   It also applies to python.


.. _rule of three: http://en.wikipedia.org/wiki/Rule_of_three_(C%2B%2B_programming)

Quivers : consistent sets of Traits
***********************************

.. note::

    Yes, it is a pun, trait = arrow <=> quiver = set of arrows. 


Inclusive Trait
***************

If a key is absent on one of the Mapping, it will be considered the neutral element. An empty list, for list, 0 for int, 0.0 for float...

The behaviour of addition and substraction is consistently deriving from the boolean algebrae meaning of **+** in a set context where + means union. 

Thus Addition and substraction are inclusive. 

Exclusive Trait
***************

Multiplication operates as an intersection, because on one hand it is consistentwith the set/boolean meaning of multiplication, and
also that neutral element of addition, is normaly the null element of multiplication. Since multiplication implies division, instead of multiplying by 0
and keeping present in at least one dict, I prefer to avoid the raging division by zero. 
In short, I try to avoid my dict to explode when dividing by 0. I am weak  I know.

Summary of the behaviours and dependancies
******************************************

=============== ===== ========= ================ ======= =====================
Operation       Short Behaviour Requires         Safe    Name
=============== ===== ========= ================ ======= =====================
Copier          copy  None         
Addition        add   Inclusive copy             Yes     InclusiveAdder
Multiplication  mul   Exclusive add,copy         Yes     ExclusiveMuler
Substraction    sub   Inclusive add,mul,copy     Yes     InclusiveSubber
Division        div   Exclusive add,mul,sub,copy No      TaintedExclusiveDiver
=============== ===== ========= ================ ======= =====================


What is addition in MutableMapping useful for?
==============================================

It is used with `yahi <http://github.com/jul/yahi>`_ as an exemple. I find addition
on MutableMapping a very convenient way to reduce by using in place addition (__iadd__). 

`VectorDict`_ also has an exemple of map/reduce with `multiprocessing word counting`_

`MapReduce`_ is a way of treating big data without consuming too much memory ensuring relativley good performance. 
It is normaly considered to belong to the functional paradigm and is best used with generators. 

.. _vectorDict: http://vectordict.readthedocs.org/en/latest/
.. _multiprocessing word counting: http://vectordict.readthedocs.org/en/latest/vector.html#word-counting-with-multiprocess-and-vector-dict
.. _MapReduce: http://en.wikipedia.org/wiki/MapReduce

Changelog and roadmap
=====================

Changelog
*********

1.1.1
    Trying very hard to have the README.rst formated.

1.1.0
    *make_from_path* : it made no sense it took a first argument
    a MutableMapping that would be destroyed in the process.
    Now takes a type of MutableMapping as an input.

1.0.0
    Flatter and simpler naming (while keeping descendant compatibility)

0.1.8
    release with better code coverage

0.1.7
    Maintenance release correcting minor bugs in preparation for
    the 1.0 release

0.1.6
    Tested py3.2 on my freeBSD, it works for me ©

0.1.4
    closes #6 : trying to install on debian stable is like contemplating a machine
    frozen 5 years ago. Rerunning tests on debian

0.1.3
    blocking install if tests don't pass

0.1.2
    py3 compliance

0.1.1
    closing issue in iadd: some performance issue in __iadd__ aka +=

0.1.0
    initial release



Convention:
***********

version x.y.z

while in beta  convention is :

- **x** = 0
- **y** = API change
- **z** = bugfix and/or improvement

and then

- **x** = API change
- **y** = improvement
- **z** = bugfix

Roadmap
*******

1.2.0
    - fixes a bug in __radd__ such as doing a+b could result in modifying
    a (a+b was acting lile a+=b)

1.1.1/2
    - trying to have a valider valid README.rst (python setup check -r is not enough)

1.0.0
    - Flattening the structure of archery and making naming more obvious
    - Keeping the old API compatible
    - Begining deprecation
    - maybe prepare a set of trait to make recursive dict looks like 
      *sets* in a consistent way


