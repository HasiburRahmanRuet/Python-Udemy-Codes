# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:12:35 2020

@author: Naznin
"""


import re
pattern=re.compile(r'Hasib')
me=pattern.match("Hasib")
me_1=pattern.search("Hasib Mirza")
me_1.group()

