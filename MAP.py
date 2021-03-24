#!/usr/bin/python
numbers = (1, 2, 3, 4) 
result = map(lambda x: x * x, numbers) 
print(list(result)) 
# Add two lists using map and lambda 
List1 = [1, 2, 3] 
List2 = [4, 5, 6] 
result = map(lambda x, y: x + y, List1,List2) 
print(list(result)) 
# Making List of tuples from two list
result=zip(List1,List2)
print "List of tuple",result

















