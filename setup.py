#!/usr/bin/env python
# -*- coding: "utf-8" -*-

from distutils.command.build_py import build_py as _build_py
from distutils.core import setup
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

if "install" in sys.argv or "sdist" in sys.argv:
 
    test()

setup(
        name='archery',
        version='0.1.5',
        author='Julien Tayon',
        author_email='julien@tayon.net',
        packages=['archery'],
        url='http://archery.readthedocs.org/',
        license=open('LICENSE.txt').read(),
        description='Traits (Mixins) to give +,/,-,* to MutableMapping ',
        requires=[ ],
        classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Python Software Foundation License',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
)
