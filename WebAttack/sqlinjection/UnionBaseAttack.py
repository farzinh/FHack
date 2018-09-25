# -*- coding: utf-8 -*-
'''
    This file contain union exploit class
'''
try:
    from src.Colors import TextColor
    from injection_defines import *
    import requests as reqs
except Exception as err:
    raise SystemExit, TextColor.RED + str("something is wrong " + err) + TextColor.WHITE

class UnionBaseAttack(object):
    def __init__(self, url, injectedChar, firstResponse):
        self.url = url
        self.injectedChar = injectedChar
        self.firstResponse = firstResponse
