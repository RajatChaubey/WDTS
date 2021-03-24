#!/usr/bin/python
squares = (x * x for x in range(1,10))
print(type(squares))
print(list(squares))
L= [x*x for x in (1,3,5,7)]
print (type(L))
print L



a_set = {1, 2, 3}
b_iterator = iter(a_set)
print "Just one value at 1st time ",next(b_iterator)
print "Just one value at 2nd time ",next(b_iterator)
print "Just one value at 3rd time ",next(b_iterator)

for i in b_iterator:
         print "using For loop here ",i

