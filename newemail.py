#!/usr/bin/python
import re
str = 'purple #alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'[\w\.-]+@[\w\.-]+', str)

print tuples
