#/usr/bin/env python
import os
import sys

import unittest
from  archery.bow import Hankyu, Daikyu
from archery.barrack import bowyer

from math import sqrt


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

    def test_add_exists(self):
        self.easy += dict(x=1)
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
if __name__ == '__main__':
    unittest.main(verbosity=2)
