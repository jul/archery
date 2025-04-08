#/usr/bin/env python
import os
import sys

import unittest
from archery.quiver import VectorDict
from archery.barrack import make_from_path, mapping_row_iter
from archery import mdict
from collections import Counter

from math import sqrt, cos, pi

class CWCos(VectorDict, Counter):
    pass

class TestCosWithCounter(unittest.TestCase):


    def testCos(self):
        self.assertAlmostEqual(
                CWCos(["mot", "wut", "wut", "bla"]).cos(CWCos(["mot","wut", "bla"])),
                0.942809041582
        )
        self.assertAlmostEqual(
                CWCos(["mot", "wut", ]).cos(CWCos(["mot",])),
                cos(pi/4)
        )

class TestBuildingFromMap(unittest.TestCase):

    def test_weired_exp_idea(self):
        tree= dict(a=dict(b=1, c=1, d=dict(e=2, f=dict(e=5)), v=3))
        self.assertEqual(tree,
                sum([ make_from_path(mdict, p) for p in mapping_row_iter(tree)])
        )

if __name__ == '__main__':
    unittest.main(verbosity=4)
