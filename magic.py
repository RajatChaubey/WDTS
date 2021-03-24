#!/usr/bin/python
## An easy to eliminate duplicate elemnt from list
list1=[1,2,3,2,4,1,3,5,7,8,9,7]
print "try", list(set(list1))
x=set(list1)
#print type(x)
lx=[]
for i in x:
     lx.append(i)
print lx
## Dict comprehension programs to print key:values as -
## even:square of even number 
dic2={n:n*n for n in range(1,11) if n%2 == 0}
print dic2
