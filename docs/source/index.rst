.. archery documentation master file, created by
   sphinx-quickstart on Wed May 16 19:22:05 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

* Source : https://github.com/jul/archery
* Tickets : https://github.com/jul/archery/issues?state=open
* Latest documentation : http://archery.readthedocs.org/en/latest/index.html

What is archery? 
================

It is set of Mixins to use on MutableMapping giving the following features :

- Linear Algebrae;
- Vector like metrics;
- Searchable behaviour;

for convenience 3 concrete classes are provided : 

- `mdict`_ (dict that follow the rules of linear algebrae based on dict);
- `vdict`_ (dict that have cos, abs, dot product);
- `sdict`_ (dict that are easily searchable);

following this inheritance graph of traits


Graph
*****

.. graphviz::

    digraph G {
        node [ shape=box ];
        splines=ortho;
       subgraph cluster_0 {
           label = "Copier";
           style=line;
           color=puprle;
           Copier;
       }
       subgraph cluster_1 {
           label = "LinearAlgebrae";
           style=line;
           color=green;
           Adder -> Muler [label = "a+.+a (n) = a * n"];
           Muler -> Suber [label = "a-n = a * -n "];
           Suber -> Diver [label = "a/n = a * 1/n" ];
       }
       Copier -> Adder [label = "generic deepcopy"];
       subgraph cluster_2 {
           Dot -> Abs -> Cos;
           style=line;
           label = "Vector";
           color=blue;
       }
       Copier -> Dot;
       Muler -> Dot;
       subgraph cluster_3 {
           label = "Searchable";
           color = red;
           iter [ label = "__iter__"];
           iter -> search ;

       }
       Copier -> iter;
       Diver ->  mdict [label = "concrete class dict" ];
       Cos -> vdict [label = "concrete class dict" ];
       search -> sdict [label = "concrete class dict" ];


    }


Basic Usage
===========

Using the ready to use class derived from dict

mdict
*****

**dict that supports consistently all the linear algebrae properties**

Basically : dict that are vectors on arbitrary basis (recursively).

To learn more about its use and implementation:

- `Video presentation in FOSDEM 2017 <https://www.youtube.com/watch?v=Rd6rY5zNcGM>`_ 
- `or look at the presentation <http://jul.github.io/cv/pres.html#printable>`_

ex::

    >>> from archery import mdict
    >>> point = mdict(x=1, y=1, z=1)
    >>> point2 = mdict(x=1, y=-1)
    >>> print( (2 * point + point2)/4)
    >>> # OUT : {'y': 0.25, 'x': 0.75, 'z': 0.5}
    >>> print(point - point2)
    >>> # OUT : {'y': 2, 'x': 0, 'z': 1}    
    >>> b=mdict(x=2, z=-1)
    >>> a=mdict(x=1, y=2.0)
    >>> a+b
    >>> # OUT: {'y': 2.0, 'x': 3, 'z': -1}
    >>> b-a
    >>> # OUT: {'y': -2.0, 'x': 1, 'z': -1}
    >>> -(a-b)
    >>> # OUT: {'y': -2.0, 'x': 1, 'z': -1}
    >>> a+1
    >>> # OUT: {'y': 3.0, 'x': 2}
    >>> -1-a
    >>> # OUT: {'y': -3.0, 'x': -2}
    >>> a*b
    >>> # OUT: {'x': 2}
    >>> a/b
    >>> # OUT: {'x': 0}
    >>> 1.0*a/b
    >>> # OUT: {'x': 0.5}

vdict
*****
    

dict that defines *abs()*, *dot()*, *cos()* in the euclidean meaning

ex::
   >>> from archery import vdict as Point
   >>>
   >>> u = Point(x=1, y=1)
   >>> v = Point(x=1, y=0)
   >>> u.cos(v)
   >>> 0.7071067811865475
   >>> u.dot(v)
   >>> # OUT: 1
   >>> u.cos(2*v)
   >>> # OUT: 0.7071067811865475
   >>> u.dot(2*v)
   >>> #OUT: 2
   >>> abs(u)
   >>> #OUT: 1.4142135623730951
   >>> u3 = Point(x=1, y=1, z=2)
   >>> u4 = Point(x=1, y=3, z=4)
   >>> u3 + u4
   >>> #OUT: dict(x=2, y=4, z=6)
   >>> assert u4 + u4 == 2*u4
   >>> from archery import vdict
   >>> from math import acos, pi
   >>> point = vdict(x=1, y=1, z=1)
   >>> point2 = vdict(x=1, y=-1)
   >>> point2 = mdict(x=1, y=-1)
   >>> print( (2 * point + point2)/4)
   >>> # OUT : {'y': 0.25, 'x': 0.75, 'z': 0.5}
   >>> print(acos(vdict(x=1,y=0).cos(vdict(x=1, y=1)))*360/2/pi)
   >>> # OUT : 45.0
   >>> print(abs(vdict(x=1, y=1)))
   >>> # OUT : 1.41421356237
   >>> print(vdict(x=1,y=0,z=3).dot(vdict(x=1, y=1, z=-1)))
   >>> #OUT -2

sdict
*****

dict made for searching value/keys/`Path`_ with special interests.

Basically, it returns an interator in the form of a tuple being all the keys and the value.
It is a neat trick, if you combine it with `make_from_path`_, it helps select exactly what you want in a dict::


    >>> from archery import sdict, make_from_path
    >>> tree = sdict(
    ...      a = 1,
    ...      b = dict(
    ...          c = 3.0,
    ...          d = dict(e=True)
    ...      ),
    ...      point = dict( x=1, y=1, z=0),
    ... )
    >>> list(tree.leaf_search(lambda x: type(x) is float ))
    >>> #Out: [3.0]
    >>> res = list(tree.search(lambda x: ("point") in x ))
    >>> ## equivalent to list(tree.search(lambda x: Path(x).contains("point")))
    >>> print(res)
    >>> #Out: [('point', 'y', 1), ('point', 'x', 1), ('point', 'z', 0)]
    >>> make_from_path(dict(), res)
    >>> # {('point', 'y', 1): {('point', 'x', 1): ('point', 'z', 0)}}


Advanced usage
==============

This library is a proof of the consistent use of Mixins on `MutableMapping <https://docs.python.org/3.7/library/collections.abc.html?highlight=mutablemapping#collections.abc.MutableMapping>`_ gives the property seen in the basic usage.


The Mixins do not require any specifics regarding the implementation and **should** work if I did my job properly with
any kinds of *MutableMapping*.

Here is an example of a cosine similarities out of the box on the *Collections.Counter* ::

    >>> from collections import Counter
    >>> from archery import VectorDict
    >>> class CWCos(VectorDict, Counter): 
    ...     pass
    >>>
    >>> CWCos(["mot", "wut", "wut", "bla"]).cos(CWCos(["mot","wut", "bla"]))
    >>> # OUT: 0.942809041582

You can also inherit LinearAlgebrae


API
===


VectorDict / vdict
******************

.. autoclass:: archery.trait.Vector
    :members: dot, __abs__, cos

Searchable, sdict
*****************

.. autoclass:: archery.trait.Searchable
    :members: search, leaf_search

Path
****

Basically a class meant for making search in `sdict`_ more readable
so that you have shortcuts that are more meaningfull than manipulating a tuple


.. autoclass:: archery.Path
    :members: endswith, startswith, key, value, contains

make_from_path
**************

.. automodule:: archery
    :members: make_from_path

mapping_row_iter
****************

.. automodule:: archery
    :members: mapping_row_iter

    
Detailed documentation
======================

Contents:

.. toctree::
   extra
   roadmap
   :maxdepth: 1



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

