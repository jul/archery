#!/usr/bin/env pyrhon
# -*- coding: "utf-8" -*-

from distutils.command.build_py import build_py as _build_py
from distutils.core import setup

def test():
    """Specialized Python source builder."""
setup(
        name='archery',
        version='1.0.0',
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
