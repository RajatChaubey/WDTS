#!/usr/bin/python
import re
str= "# my name is # RAJAT # chaubey#"

r = re.sub(r'#+', "", str)
print r
