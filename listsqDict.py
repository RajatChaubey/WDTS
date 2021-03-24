#!/usr/bin/python

list1=[2,3,4,5,6]
dict1={k:k*k for k in list1}

print dict1.items()
print type(dict1)
print "Dictionary keys:",len(dict1.items())
