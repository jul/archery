#!/usr/bin/env python
# -*- coding: "utf-8" -*-

#from setuptools import setup, find_packages
#import unittest
#import sys
from distutils.command.build_py import build_py as _build_py
from distutils.core import setup
from archery import __version__
from archery import __author__
from archery import __author_email__
import unittest
import sys

def test():
    """Specialized Python source builder."""
    from archery import test_archery
    loader= unittest.TestLoader()
    suite=loader.loadTestsFromModule(test_archery)
    runner=unittest.TextTestRunner()
    result=runner.run(suite)
    if  not result.wasSuccessful():
        raise Exception( "Test Failed: Aborting install")

if "install" in sys.argv or "sdist" in sys.argv or "update" in sys.argv:
 
    test()

setup(
        name='archery',
        version=__version__,
        author=__author__,
        author_email=__author_email__,
        packages=['archery'],
        url='http://archery.readthedocs.org/',
        license=open('LICENSE.txt').read(),
        description='Traits (Mixins) to give +,/,-,* to MutableMapping ',
        long_description=open("README.txt").read(),
        requires=[ ],
        classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: Python Software Foundation License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
)
