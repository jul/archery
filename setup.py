#!/usr/bin/env python
# -*- coding: "utf-8" -*-

#from setuptools import setup, find_packages
#import unittest
#import sys
from distutils.command.build_py import build_py as _build_py
from distutils.core import setup
from distutils.cmd import Command
from archery import __version__
from archery import __author__
from archery import __author_email__
import unittest
import sys

class Test(Command):
  """A custom command to run Pylint on all Python source files."""
  def initialize_options(self):
    """Set default values for options."""
    self.verbosity=1
    pass

  def finalize_options(self):
    """Post-process options."""
    pass

  description = 'test the module'
  user_options = [
  ('verbosity=', 'V', 'verbosity level'),
  ]


  def run(self):
    """Run command."""
    test(int(self.verbosity))

def test(verbosity=1):
    """Specialized Python source builder."""
    from archery import test_archery
    loader= unittest.TestLoader()
    suite=loader.loadTestsFromModule(test_archery)
    runner=unittest.TextTestRunner(verbosity=verbosity)
    result=runner.run(suite)
    if  not result.wasSuccessful():
        raise Exception( "Test Failed: Aborting install")

if "install" in sys.argv or "sdist" in sys.argv or "update" in sys.argv:
    test()

setup(
        cmdclass=dict(
        test=Test,
        ),
        name='archery',
        version=__version__,
        author=__author__,
        author_email=__author_email__,
        packages=['archery'],
        url='http://archery.readthedocs.org/',
        license="Python Software Foundation License",
        description='Traits (Mixins) to give +,/,-,* to MutableMapping ',
        long_description=open("README.txt").read(),
        requires=[ ],
        scripts = ( "archery/toy/big", ),
        classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: Python Software Foundation License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
)
