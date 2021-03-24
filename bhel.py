#!/usr/bin/python
from string import maketrans
dict={'a':1,'b':2,'c':3}
L=[(k,v) for (k,v) in dict.items()]
print ''' This is to check 
what it sows \n nad what not\t4''' ,L
#d=dict(L)
print u'Hello\u0020World !#Now back to form!'
print "#Now back to form!"
#


#intab = "rajat"
#outtab = "NAAJI"
#trantab =maketrans(intab, outtab)
str = "this is string example....wow ZZ rajat";
#print str.translate(trantab),"min",
print str.replace("is\b", "was");

