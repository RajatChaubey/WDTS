#!/usr/bin/python
import re

EmailID = 'rajnarayan.chaubey@gmail.com'
match = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', EmailID, re.I)
#print match.group()
if (match):
   print "Its a valid"
else:
   print "Not Valid"
############## FURTHER ENHANCED ###################

match = re.search(r'[\w.-]+@[\w.-]+', EmailID)
if match:
    print match.group()  

######################## use of group to seggregate from user n domain ####
match = re.search(r'([\w.-]+)@([\w.-]+)', EmailID)
if match:
    print match.group()   ##  (the whole match- email id)
    print match.group(1)  ## 'rajnarayan.chaubey' (the username, group 1)
    print match.group(2)  ## 'gmail.com' (the host, group 2)




