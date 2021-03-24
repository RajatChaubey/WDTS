#!/usr/bin/python

import re


xx = "guru92 raja abrajar raswa ram rajdhani ramesh RAJat raj"
r1 = re.findall(r'(\braj\w+)',xx,re.I)
print(r1)
