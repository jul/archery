Trait are Mixins
****************

Trait are Mixins, behaviour. All these terms recovers loosely the same idea.

In this case refering to even older conventions traits are concrete classes for abstract classes/interfaces. 

collections.MutableMapping defines an interface and some concrete methods. Since isinstance relies on interfaces (ducktyping) 
I can safely use it to implement methods that don't exists and will normally work for most Mappings. 

.. warning: Traits relies on copy, if ever you define a custom constructor, don't forget the `rule of three`_. 
   It also applies to python.


.. _rule of three: http://en.wikipedia.org/wiki/Rule_of_three_(C%2B%2B_programming)


InclusiveAdding and Subbing
===========================

Generic behaviour
-----------------

Addition is propagated for each keys of both Mappings and will be propagated to the values. 
If the values are MutableMapping with addition they will propagate to the keys.
If the values are not MutableMapping they will be added. 

.. warning: If your MutableMapping with Addition is made of MutableMapping without it, you'll be told
   that MutableMappings do not support Addition. To solve the problem use :ref:`bowyer`

Same goes with the substraction. 

Inclusion
---------

If a key is absent on one of the Mapping, it will be considered the neutral element. An empty list, for list, 0 for int, 0.0 for float...

The behaviour of addition is consistently deriving from the boolean algebrae meaning of **+** in a set context where + means union. 

Scalar addition
---------------



Exclusive Multiplication
========================

Generic behaviour
-----------------

For each keys in both operand, values are multplied. If operand are MutableMappings with Multiplication, they will therefore propagate. 

Exclusion
---------

Multiplication also operates as an intersection, because on one hand it is consistent with considering also a set meaning of multiplication, and
also that neutral element of addition, is normaly the null element of multiplication. Since multiplication implies division, instead of multiplying by 0
and keeping present in at least one dict, I prefer to avoid the raging division by zero. 




