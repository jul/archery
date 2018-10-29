.. archery documentation master file, created by
   sphinx-quickstart on Wed May 16 19:22:05 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

* Source : https://github.com/jul/archery
* Tickets : https://github.com/jul/archery/issues?state=open
* Latest documentation : http://archery.readthedocs.org/en/latest/index.html

What is archery? 
================

It is an enhancement of MutableMapping based on Mixins. It currently only offers:

- Linear Algebrae;
- Vector like metrics;
- Searchable behaviour;

for convenience 3 usable classes are offered as a an helper : 

- mdict (dict that follow the rules of linear algebrae based on dict);
- vdict (dict that have cos, abs, dot product);
- sdict (dict that are easily searchable);

following this inheritance graph of traits


.. graphviz::

    digraph G {
        node [ shape=box ];
        splines=ortho;

       subgraph cluster_0 {
           label = "LinearAlgebrae";
           style=line;
           color=green;
           Adder -> Muler [label = "a+.+a (n) = a * n"];
           Diver -> Muler [label = "a/n = a * 1/n" ];
           Suber -> Muler [label = "a-n = a * -n "];
       }
       subgraph cluster_1 {
           Dot -> Abs -> Cos;
           style=line;
           label = "Vector";
           color=blue;
       }
       Muler -> Dot;
       subgraph cluster_3 {
           label = "Searchable";
           color = red;
           iter [ label = "__iter__"];
           iter -> search ;

       }
       Muler ->  mdict [label = "concrete class dict" ];
       mdict -> vdict [label = "derived from mdict" ];
       Cos -> vdict;
       search -> sdict [label = "concrete class dict" ];


    }

Feel free to build your own as shown in examples with Counter.


Detailed documentation
======================

Contents:

.. toctree::
   content
   bow
   trait
   quiver
   barrack
   faq
   roadmap
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

