#/usr/bin/env python
import os
import sys

import warnings
import unittest
from  archery.bow import Hankyu, Daikyu, sdict, vdict, mdict, edict
from archery.barrack import bowyer, Path, make_from_path, paired_row_iter

from math import sqrt, cos, pi, sin, acos

class TestDeprecation(unittest.TestCase):
    def test_deprec_edict(self):
        """ edict (ExpDict is becoming searchable """
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            edict(x=1)
            self.assertTrue(
                issubclass(w[-1].category, DeprecationWarning),
            )

class TestKyleExpectation(unittest.TestCase):

    def test_commutativity(self):
        a = mdict({"a": 1, "y": {"b": 4, "c": [5]}})
        b=  mdict({"a": 1, "x": 5, "y": {"b": 6, "c": [12]}})
        expected_ab = {"a": 2, "x": 5, "y": {"b": 10, "c": [5, 12]}}
        expected_ba = {"a": 2, "x": 5, "y": {"b": 10, "c": [12, 5]}}
        self.assertEqual(a + b, expected_ab)
        a = mdict({"a": 1, "y": mdict({"b": 4, "c": [5]})})
        b=  mdict({"a": 1, "x": 5, "y": mdict({"b": 6, "c": [12]})})
        self.assertEqual(b + a, expected_ba)
        a = mdict({"a": 1, "y": mdict({"b": 4, "c": [5]})})
        b=  mdict({"a": 1, "x": 5, "y": mdict({"b": 6, "c": [12]})})
        a += b
        self.assertEqual(a, expected_ab)


    def test_bug_iadd(self):
        a = mdict({"a": 1, "y": mdict({"b": 4, "c": [5]})})
        b=  mdict({"a": 1, "x": 5, "y": mdict({"b": 6, "c": [12]})})
        expected_ab = {"a": 2, "x": 5, "y": {"b": 10, "c": [5, 12]}}
        expected_ba = {"a": 2, "x": 5, "y": {"b": 10, "c": [12, 5]}}
        a += b
        self.assertEqual(a, expected_ab)
        self.assertEqual(a + b, expected_ab)
        self.assertEqual(b + a, expected_ba)


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

class TestBarrack(unittest.TestCase):
    def test_path(self):
        self.assertEqual(
            Path(("a","b",1)).key(),
            ("a","b")
        )
        self.assertFalse(
            Path(("a","b",1)).contains("a","b","c")
        )
        self.assertEqual(
            Path(("a","b",1)).value(),
            1
        )
        self.assertTrue(Path(("x", "y", 1)).startswith("x"))
        self.assertTrue(Path(("s", "x", "y", 1)).contains("x","y"))

    def test_paired_row_iter(self):
        self.assertEqual(set(paired_row_iter(dict(x=1, a=dict(b=dict(c=1))))),
            { (("x",),1), (("a","b","c"), 1)}
        )


class TestBugWeired(unittest.TestCase):

    def test_stay_same(self):

        class Matrix(mdict):
            def __call__(self, other):
                other = other.copy()
                res= vdict()
                for (src, dst), functor in self.items():
                    res += mdict({ dst: functor(other[src])})
                return res


        theta = pi/6

        u = mdict(x=1, y=2)
        v = mdict(x=1, y=0)
        alien = vdict(x=u, y=v)

        def rotation_maker(theta):
            """"Matrix takes as key (SRC, DST) (which is the opposite of "actual notation")
            """
            return Matrix({
                ("x", "x") : lambda v:1.0 *  v * cos(theta),
                ("y", "x") : lambda v:1.0 * -v * sin(theta),
                ("x", "y") : lambda v:1.0 *  v * sin(theta),
                ("y", "y") : lambda v:1.0 *  v * cos(theta)
            })

        rotation = rotation_maker(pi/6)
        self.assertAlmostEqual(
            rotation(u),
            {'x': -0.13397459621556118, 'y': 2.232050807568877}
            )
# OUT:{'x': 1, 'y': 0}
        self.assertAlmostEqual(rotation(v),
            {'x': 0.8660254037844387, 'y': 0.49999999999999994}
        )
        self.assertAlmostEqual(
            acos(vdict(u).cos(vdict(rotation(u))))/2 / pi * 360,
            29.999999999999993
        )
        self.assertEqual(u, dict(x=1, y=2))
        self.assertAlmostEqual(acos(vdict(v).cos(vdict(rotation_maker(pi/3)(v))))/2 / pi * 360,
60.0)
        self.assertAlmostEqual(
            acos(vdict(v).cos(vdict(rotation_maker(pi/5)(v))))/2 / pi * 360,
            36.0
        )
        self.assertEqual(
            alien,
            {'x': {'x': 1, 'y': 2}, 'y': {'x': 1, 'y': 0}}
        )
        """
        undefined behaviour until I can make a sense of this



        self.assertAlmostEqual(
            rotation_maker(pi/4)(alien),
            {
                'x': {'x': 1.1102230246251565e-16, 'y': 1.4142135623730951},
                'y': {'x': -1.1102230246251565e-16, 'y': 1.414213562373095}
            }
        )
        self.assertAlmostEqual(
            acos(alien.cos(rotation_maker(pi/4)(alien)))/2 / pi * 360,
            54.73561031724534
        )

        self.assertAlmostEqual(rotation_maker(pi/4)(alien),
            {'x':
                {'x': 1.1102230246251565e-16, 'y': 1.4142135623730951},
             'y': {'x': -1.1102230246251565e-16, 'y': 1.414213562373095}})
        """


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
        does not converts it on the fly to himself"""
        self.assertNotEqual(
            type(self.tree["point"]),
            sdict
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
        self.assertEqual(
                set([ x for x in self.tree.search(
                    lambda x : Path(x).startswith("a")
                    )
                ]),
                set([('a', 1)])
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
