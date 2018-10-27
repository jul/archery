#!/usr/bin/env python
# -*- coding: utf8 -*-
"""Making dict great vectors!


"""

from .bow import Daikyu as mdict, vdict
from .bow import edict
from .barrack import paired_row_iter, bowyer
__version__ = "0.1.7"
__all__ = [
    "__version__", "dot", "abs", "cos", "mdict", "paired_row_iter", "edict" ]



