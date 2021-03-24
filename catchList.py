#!/usr/bin/python

list=[1,2,3,[4,5,6],3,56,77,8,[34,55],55,66,77]

print "val",list[8][0]

l1=[2,3,4]
l2=[3,5,7]
l3=zip(l1,l2)
print "zipped ",l3

l4=[(l1[i],l2[i]) for i in range(0,len(l1))]

print "l4",l4


def x(*a):
    for i in a:
      print "arguements",i



x('a','b','c')
