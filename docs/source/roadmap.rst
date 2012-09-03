Changelog and roadmap
=====================

Changelog
*********

0.1.0
    initial release

0.1.1
    closing `issue5`_ : some performance issue in __iadd__ aka +=

0.1.2
    py3 compliance

0.1.3
    blocking install if tests don't pass

0.1.4
    closes #6 : trying to install on debian stable is like contemplating a machine
    frozen 5 years ago. Rerunning tests on debian

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

Maybe backporting the search find and replace feature of `VectorDict`_

.. _VectorDict: http://vectordict.readthedocs.org
.. _issue5: https://github.com/jul/archery/issues/5
