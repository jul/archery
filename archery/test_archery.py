#/usr/bin/env python
import os
import sys

import unittest
from  archery.bow import Hankyu, Daikyu, sdict, vdict
from archery.barrack import bowyer, Path

from math import sqrt, cos, pi



class TestVectorDict(unittest.TestCase):
    """test a dict with Vector properies (cos, dot, abs)"""

    def setUp(self):
        self.point = vdict( x=3, y=3, z=0)
        self.point2 = vdict( x=1, y=1, z=1)
    
    def testNorm(self):
        self.assertAlmostEqual(
                abs(self.point),
                sqrt(3*3+3*3)
        )
    def testCos(self):
        self.assertAlmostEqual(
                vdict(x=1,y=0).cos(vdict(x=1,y=1)),
                cos(pi/4)
        )



class TestSearchableDict(unittest.TestCase):
    def setUp(self):
        self.easy = vdict( x=1, y=1, z=0)
        
        self.tree = sdict(
            a = 1,
            b = dict(
                c = 3.0,
                d = dict(e=True)
            ),
            point = self.easy
        )
    

    def test_rec_type(self):
        """test that if created with another mutale mapping
        converts it on the fly to himself"""
        self.assertEqual(
            type(self.tree["point"].copy()),
            sdict
        )

    def test_propagate(self):
        self.tree.propagate(
                lambda v: type(v) in { float, int},
                lambda v: 2 * int(v),
                lambda v: v
            )
        self.assertEqual(
                self.tree["point"]["x"],
                2
        )
        self.assertEqual(
                self.tree["b"]["c"],
                6 
        )

    def test_apply(self):
        self.tree.apply(lambda x : x+1)
        self.assertEqual(
            self.tree["b"]["c"],
            5.0
        )
        self.assertEqual(
            self.tree["b"]["d"]["e"],
            4
        )

    def test_search(self):
        self.assertEqual(
                set([ x for x in self.tree.search(
                    lambda x : Path(x).contains("point","x") 
                        or Path(x).endswith(3.0)
                    )
                ]),
                set([('b', 'c', 3.0), ('point', 'x', 1)])
        )

    def test_leaf_search(self):
        self.assertEqual(
                [ i for i in self.tree.leaf_search(lambda x : type(x) is  float)],
                [ 3.0 ]
        )
        self.assertEqual(
                [ i for i in self.tree.leaf_search(lambda x : type(x) is  bool)],
                [ True ]
        )
        


        

class TestHankyu(unittest.TestCase):
    def setUp(self):
        self.easy = Hankyu( x=1, y=1, z=0)
        self.easy_too = Hankyu( x=0, y=-2, o=0)
        
        self.a_tree = dict(
            a = 1,
            b = dict(
                c = 3.0,
                d = dict(e=True)
            ),
            point = self.easy
        )
        self.cplx = bowyer(Hankyu,self.a_tree)

    def test_convert(self):
        self.assertEqual(
            bowyer(Hankyu, {'a': {'b': 1}}),
            Hankyu( {'a': Hankyu(b=1)})
            )
        

    def test_add_not_exists(self):
        self.easy += dict(a=1)
        self.assertEqual(self.easy['a'], 1)
        self.assertEqual(
                self.easy + self.easy_too, 
                sum([ self.easy_too, self.easy])
        )

    def test_add_exists(self):
        self.easy += dict(x=1)
        self.assertEqual(self.easy['x'] , 2)

    def test_number_inc(self):
        self.easy += 1
        self.assertEqual(self.easy['x'] , 2)


    def test_bug_convert_empty_mapping(self):
        """bug #8 : empty mapping intialisation dont work"""
        bug = bowyer( Hankyu,dict( a={}))
        expected = Hankyu( {'a': {}})
        self.assertEqual(
            expected,
            bug
        )

class TestDaikyu(unittest.TestCase):
    def setUp(self):
        self.easy = Daikyu( x=1, y=1, z=0)
        self.easy_too = Daikyu( x=0, y=-2, o=0)
        
        self.a_tree = dict(
            a = 1,
            b = dict(
                c = 3.0,
                d = dict(e=True)
            ),
            point = self.easy
        )
        self.cplx = bowyer(Daikyu,self.a_tree)


    def test_bug_1(self):
        """bug  #1 : * returns a copy where a reference is needed"""
        pt = self.easy
        pt *= -1
        self.assertEqual(
            self.easy,
            pt
        )
    def test_bug_2(self):
        """bug #2 : self * other without affectation should not modify self.
        """
        self.easy *= -1
        a_copy = self.easy.copy()
        self.easy * a_copy
        self.assertEqual(
            self.easy,
            a_copy
        )


    def test_bug_4(self):
        """bug #4 : self / other without affectation should not modify self.
        """
        del(self.easy['z'])
        self.easy /= -1
        a_copy = self.easy.copy()
        self.easy / a_copy
        self.assertEqual(
            self.easy,
            a_copy
        )

    def test_bug_5(self):
        """bug #5 : int * dict without affectation should not modify self.
        """
        a_copy = self.easy.copy()
        2 * self.easy
        self.assertEqual(
            self.easy,
            a_copy
        )

    def test_bug_6(self):
        """bug #6 : int / dict without affectation should not modify self.
        """
        del(self.easy['z'])
        a_copy = self.easy.copy()
        2.0 / self.easy
        self.assertEqual(
            self.easy,
            a_copy
        )


    def test_for_fun(self):
        """just for fun """
        a = self.easy
        b = self.easy_too
        aa = a.copy()
        bb = b.copy()
        self.assertEqual(
            (a - b) * (a + b),
            aa * aa - bb * bb
        )


    def test_for_fun2(self):
        """just for fun """
        a = self.easy
        b = self.easy_too
        aa = a.copy()
        bb = b.copy()
        self.assertEqual(
            -(a + b) * (a + b),
            -1 * ((aa * aa) + 2 * aa * bb + (bb * bb))
        )
    
    def test_dyslexia_bug4(self):
        """counfonding right & left in all r(div/add/sub/mul) operator """
        a = self.easy
        self.assertEqual(
            2/Daikyu({'a':1}),
            {'a' : 2}
        )
        self.assertEqual(
            2-a,
            -(a-2)
        )
    def test_inplace_bug5(self):
        """a/b in place"""
        a = self.easy*4
        self.assertEqual(
            a/{'x':2},
            {'x' : 2}
        )

if __name__ == '__main__':
    unittest.main(verbosity=4)
