#!/usr/bin/env python
# -*- coding: utf8 -*-
"""Making dict great vectors!
"""

from .bow import mdict, vdict, sdict
from .barrack import (
    paired_row_iter, bowyer, make_from_path, Path, mapping_row_iter
)
__version__ = "1.1.1"
__author__ = "julien tayon"
__author_email__ = "julien@tayon.net"
__all__ = [
     "__version__", "vdict","sdict", "mdict", "paired_row_iter", 
     "mapping_row_iter", "__author__", "__author_email__"]



