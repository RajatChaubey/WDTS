#!/usr/bin/python
import re
x="10.22.23.40"
# use highlighted  expression 4 times,OPERATOR ^ just one time and concat with \.
obj=re.search(r'(^[25[0-5]|2[0-4][0-9]|[0-1]?|[0-9][0-9]?)\.([25[0-5]|2[0-4][0-9]|[0-1]?|[0-9][0-9]?)\.([25[0-5]|2[0-4][0-9]|[0-1]?|[0-9][0-9]?)\.([25[0-5]|2[0-4][0-9]|[0-1]?|[0-9][0-9]?)$',x)
if obj: 
   print "Matched"
else:
   print "NOT MATCHED" 


