.. archery documentation master file, created by
   sphinx-quickstart on Wed May 16 19:22:05 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

* Source : https://github.com/jul/archery
* Tickets : https://github.com/jul/archery/issues?state=open
* Latest documentation : http://archery.readthedocs.org/en/latest/index.html

What is archery? 
================

Is a functional rewrite of VectorDict (https://github.com/jul/ADictAdd_iction) that was
becoming unmaintainable because it was a little bit too complex.

It is also an illustration of the use of mixins with interface/abstract collections.

Last but no least, it is fun, and usable. 

archery.trait
*************

Traits are the Perl equivalent of mixins (ruby behaviour).
The mixins in archery are dedicated to provide customisable operator on 
mapping for : 

* addition,
* substraction,
* division,
* multiplication

*archery.trait* provides individual trait. 

archery.quiver
**************

A **quiver** is a set of traits lovingly assembled so that they are consistent.

archery.bow
***********

Ready made MutableMapping (dict) that supports addition. 

archery.barrack
***************

Misc utilities. 

Who needs archery?
==================

* people wanting to experiment what a good addition on any MutableMapping 
(dict included) coud be (**trait** documentation is for them);
* people wanting to have a consistent set of operations for their MutableMapping (**quiver** is for them);
* those who wants ready made dict pretty practical for map/reduce (**bow** is for them).


Detailed documentation
======================

Contents:

.. toctree::
   foreword
   trait
   quiver
   weapon
   version
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

