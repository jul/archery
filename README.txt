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


What's new
**********

* py3 compliance;
* install is blocked if tests are failing with pip
* install is blocked if tests are failing with easy_install

Resource
********

Ticketing: https://github.com/jul/archery/issues?state=open
Source: https://github.com/jul/archery
Latest documentation: http://archery.readthedocs.org/en/latest/index.html
