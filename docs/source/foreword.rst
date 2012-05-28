Foreword
********

What is addition in MutableMapping useful for?
=======================================

It is used with `parseweblog`_ as an exemple. I find addition
on MutableMapping a very convenient way to reduce by using in place addition (__iadd__). 

`VectorDict`_ also has an exemple of map/reduce with `multiprocessing word counting`_

`MapReduce`_ is a way of treating big data without consuming too much memory ensuring relativley good performance. 
It is normaly considered to belong to the functional paradigm and is best used with generators. 

.. _vectorDict: http://vectordict.readthedocs.org/en/latest/
.. _multiprocessing word counting: http://vectordict.readthedocs.org/en/latest/vector.html#word-counting-with-multiprocess-and-vector-dict
.. _MapReduce: http://en.wikipedia.org/wiki/MapReduce
.. _parseweblog: https://github.com/jul/parseweblog

Doesn't it overlaps with defaultdict?
=====================================

No. Results seems similar, but the collections.defaultdict philosophy is different and does not mix in very well with archery because
you have a conflict. I therefore admit, there is a design flaw in VectorDict. 

defaultdict creates missing key from a factory (a function with void argument) and will consider that asking for a key that does not exists makes it real. 

MutableMapping with the default traits will raise an Exception in such case, however, if you add to MutableMapping, as the default Adder is Inclusive, it will add
the exisiting key of the source and destination. No values in MutableMapping with the default Adder will exists unless there are already defined in the MutableMappings. 

Since traits are flexible, You or I could provide more stricts dict. 

**Trait seems to provide `autovivification`_ but it does not ! No values will be created on the fly.**

As a result, there is a conflict between defaultdict and traits : for instance with a defaultdict when you add with a value that does not exists in one of 
the dict you should use the default factory. With actual traits, it is assumed the value is the neutral element of addition, thus having far less problems
than with defaultdict. 

.. _autovivification: http://en.wikipedia.org/wiki/Autovivification

Why so much fuss on Algebrae if you use Addition 99% of the time?
=================================================================

Because Algebrae is not about knowing the value of 1 + 1, it is about consistency rules for operator. People
usually focus on the operand of an operation to check if it works, I focus on the operator behaviour and how
well they behave together. Mathematical symbols are a litterature whose intuition can safely work
if we stay in the safeguard of the acceptable behaviour. These behaviours are commonly refered: distributivity, neutral element, scalar
multiplication (or linear combinations), associativity.

Algebrae, is as a result for me only a functional test for the macro behaviour of addition. Addition alone has 
**strictly** no sense. 

What is your naming convention, and what is archery exactly?
============================================================


It is all explained her : 
http://beauty-of-imagination.blogspot.com/2012/05/joice-and-headache-of-naming.html


Why do you ask to sign a legal disclaimer with my blood and sign a pact with Satan if I want to use div?
=========================================================================================================


We you look into the abyss, the abyss look into you:
http://beauty-of-imagination.blogspot.fr/2012/05/dividing-is-not-as-easy-at-it-seems.html

Using division will make you lose your sanity and your confidence in computers reliability. Unless, 
you are fully prepared for this, and you have agreed I warned you, and you really know what you are doing :
**I warn you to avoid using division on MutableMapping.**

I can use div since I don't fear losing what I am deprived of (sanity).


