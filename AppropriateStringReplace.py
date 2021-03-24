#!/usr/bin/python
import re
Line = "This is string example....wow!!! She is my Sister";
splitted=Line.split() #You can use any delimeter in () using "" default is space
print "Split gives you an Array:",splitted  

y="-".join(splitted)          
print y ," \n"

result=re.sub(r'\bis\b',"IS",Line)
print "Expectation:", result


