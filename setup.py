#!/usr/bin/env python
# -*- coding: "utf-8" -*-

from distutils.command.build_py import build_py as _build_py
from distutils.core import setup
import unittest
import sys

def test():
    """Specialized Python source builder."""
    loader= unittest.TestLoader()
    suite=loader.discover(".", "test_archery.py")
    runner=unittest.TextTestRunner()
    result=runner.run(suite)
    if  not result.wasSuccessful():
        raise Exception( "Aborting install")


if "install" in sys.argv:
    test()

setup(
        name='archery',
        version='0.1.2',
        author='Julien Tayon',
        author_email='julien@tayon.net',
        packages=['archery'],
        url='http://archery.readthedocs.org/',
        license='LICENSE.txt',
        description='Traits (Mixins) to give +,/,-,* to MutableMapping ',
        requires=[ ],
        classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Python Software Foundation License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          ],
)
