#!/usr/bin/python 
 
str = "this is string example....wow!!! this is really string"; 
print str.replace(r'"is"', "was"); 
print str.replace("is", "was", 3); 


import re
x=re.sub(r'\bin\b', 'IN', 'office administration in delhi')
print x
