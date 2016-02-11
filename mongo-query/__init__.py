# -*- coding: utf-8 -*-
import re as rex

__version__ = '0.01'

METHODS = dict()

METHODS["like:string"] = lambda fn, val: {fn: rex.compile(rex.escape(unicode(val)))}
