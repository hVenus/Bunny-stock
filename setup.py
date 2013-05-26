__author__ = 'keysentence'

from distutils.core import setup
import py2exe

setup(
    windows=['stock.py'],
    options = {
      "py2exe": {"dll_excludes":["MSVCP90.dll"]}
    }
)


