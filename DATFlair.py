#!/usr/bin/python
x=["ab","cd"]
print map(list,x)
print"result",len(map(list,x))

print "Reduce result =",reduce(lambda x,y:x-y,[1,2,3,4,5])

lis = [ 1 , 3, 5, 7, 2, 2] 
  
# using reduce to compute sum of list 
print "The sum of the list elements is : ", 
print (reduce(lambda a,b : a+b,lis))
print (list(itertools.accumulate(lis,lambda x,y : x+y)))
# using reduce to compute maximum element from list 
print "The maximum element of the list is : ",
print reduce(lambda a,b : a if a > b else b,lis)
#Remember putting "," at the end in python 2 print statment 
#will print the next print statement in same line
#Always remember a print statement always ends with \n line 
#so escape this behaviour you have to use "," in python 2 and 
# end ="" in python 3
