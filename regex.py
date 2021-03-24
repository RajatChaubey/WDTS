#!/usr/bin/python
import re

string = 'hello 12 hi 89. Howdy 34'
#pattern = '\d+'

result = re.search(r'(\d+)', string) 
print result.group()




line="pure Pyare lal is in Paris to Protect him self from pain "

mo=re.findall(r'[pP]\w+',line)
print mo

