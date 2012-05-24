.. archery documentation master file, created by
   sphinx-quickstart on Wed May 16 19:22:05 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Source : https://github.com/jul/archery
Tickets : https://github.com/jul/archery/issues?state=open
Latest documentation : http://archery.readthedocs.org/en/latest/index.html

What is archery? 
================

Is a functional rewrite of VectorDict (https://github.com/jul/ADictAdd_iction) that was
becoming unmaintainable because it was a little bit too complex.

archery.trait
*************

Traits are the Perl equivalent of mixins.
The mixins in archery are dedicated to provide customisable operator on 
mapping for : 
 * addition,
 * substraction,
 * division,
 * multiplication

_archery.trait_ provides individual trait. 

archery.quiver
**************

A *quiver* is a set of traits lovingly assembled so that they are consistent.

archery.bow
***********

Ready made Mapping (dict) that supports addiction. 

archery.barrack
***************

Misc utilities. 

Who needs archery?
==================

* people wanting to experiment what a good addition on any Mapping (dict included) coud be (*trait* documentation is for them);
* people wanting to have a consistent set of operations for their Mapping (*quiver* is for them);
* those who wants ready made dict pretty practical for map/reduce (*bow* is for them).



Welcome to archery's documentation!
===================================

Contents:

.. toctree::
   forewords
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

