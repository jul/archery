#/usr/bin/env python
import os
import sys

import unittest
from quiver import VectorDict
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


if __name__ == '__main__':
    unittest.main(verbosity=4)
