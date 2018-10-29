.. image:: https://travis-ci.org/jul/archery.svg?branch=master
    :target: https://travis-ci.org/jul/archery

.. image:: https://badge.fury.io/py/archery.svg
    :target: https://badge.fury.io/py/archery

.. image:: https://codecov.io/gh/jul/archery/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/jul/archery

.. image:: https://readthedocs.org/projects/archery/badge/?version=latest
    :target: https://archery.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


.. image:: https://img.shields.io/badge/py2.7|3.3|3.4|3.5|3.6|3.7-ok-brightgreen.svg

Description
***********

It is an enhancement of MutableMapping based on Traits (Mixins).
It makes dict addition therefore possible. 

It currently only offers:
 
* addition;
* substraction;
* multiplication;
* division.

Quick Example
*************

 dict with addition used here : http://github.com/jul/yahi

It instanciate like a dict::
    >>> from archery import mdict
    >>> a = mdict(x=1,y=2,z=2)

It adds :) ::
    >>> a+a
    {'y': 4, 'x': 2, 'z': 4}
    >>> a+-2
    {'y': 0, 'x': -1, 'z': 0}
    >>> a+.5
    {'y': 2.5, 'x': 1.5, 'z': 2.5}
    >>> .5+a
    {'y': 2.5, 'x': 1.5, 'z': 2.5}



Resource
********

Ticketing: https://github.com/jul/archery/issues?state=open
Source: https://github.com/jul/archery
Latest documentation: http://archery.readthedocs.org/en/latest/index.html
