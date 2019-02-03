from __future__ import absolute_import, print_function
import os
import sys

try:
    print("Trying import development settings...", file=sys.stderr)
    from .development import *
except ImportError:
    print("Trying import production settings...", file=sys.stderr)
    from .production import *
