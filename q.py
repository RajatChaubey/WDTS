#!/usr/bin/python

x="10.23.45.57"
flag=1
x=x.split('.')
for i in x:
    if int(i) > 255:
       print "Not a valid IP"
       flag=0
       break

if flag ==1: print "Valid IP"
