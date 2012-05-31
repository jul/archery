Traits are Mixins
*****************

Traits are Mixins, behaviours. All these terms recovers loosely the same idea.

In this case refering to even older conventions traits are concrete classes for abstract classes/interfaces. 

collections.MutableMapping defines an interface and some concrete methods. Since isinstance relies on interfaces (ducktyping) 
I can safely use it to implement methods that don't exists and will normally work for most Mappings. 

.. warning: Traits relies on copy, if ever you define a custom constructor, don't forget the `rule of three`_. 
   It also applies to python.


.. _rule of three: http://en.wikipedia.org/wiki/Rule_of_three_(C%2B%2B_programming)


General Rules:
==============

Generic behaviour
-----------------

The Operation is propagated for each keys of both Mappings and will be propagated to the ending values. 
If the values are MutableMapping with the operation they will propagate.
If the values are not MutableMapping with the trait, the operation will apply in place. 

.. warning:: If your MutableMapping with Addition is made of MutableMapping
   without it, you'll have a problem. To solve the problem use :ref:`bowyer`_


Scalar Operations
-----------------

A scalar is everything that is not a MutableMapping.  Trait support things such
as integer, array operation by applying the operation on each values of the 
MutableMapping. Order is respected. 



Inclusive Trait
---------------

If a key is absent on one of the Mapping, it will be considered the neutral element. An empty list, for list, 0 for int, 0.0 for float...

The behaviour of addition and substraction is consistently deriving from the boolean algebrae meaning of **+** in a set context where + means union. 

Thus Addition and substraction are inclusive. 

Exclusive Trait
---------------

Multiplication operates as an intersection, because on one hand it is consistentwith the set/boolean meaning of multiplication, and
also that neutral element of addition, is normaly the null element of multiplication. Since multiplication implies division, instead of multiplying by 0
and keeping present in at least one dict, I prefer to avoid the raging division by zero. 
In short, I try to avoid my dict to explode when dividing by 0. I am weak  I know.

Resumé
******

=============== ===== ========= ================ ======= =====================
Operation       Short Behaviour Requires         Safe    Name
=============== ===== ========= ================ ======= =====================
Copier          copy  None         
Addition        add   Inclusive copy             Yes     InclusiveAdder
Multiplication  mul   Exclusive add,copy         Yes     ExclusiveMuler
Substraction    sub   Inclusive add,mul,copy     Yes     InclusiveSubber
Division        div   Exclusive add,mul,sub,copy No      TaintedExclusiveDiver
=============== ===== ========= ================ ======= =====================

Why is dividing unsafe?
***********************

http://beauty-of-imagination.blogspot.fr/2012/05/dividing-is-not-as-easy-at-it-seems.html

Do you plan on adding more trait?
*********************************

I can, I still have a lot of inspiration left in `VectorDict`_ to use. 

.. _vectorDict: http://vectordict.readthedocs.org/en/latest/


