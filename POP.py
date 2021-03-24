#!/usr/bin/python 
 
aList = ['raja','rani','gulam',123, 'xyz', 'zara', 'abc']; 
 
print "Last element deleted from List : ", aList.pop(); 
print "First element will be deleted,even using POP(index_numer): ", aList.pop(0); 

print aList

bList = [123, 'xyz', 'zara', 'abc'] 
 
bList.insert(1,2020)# Insert gives you flexbility to inser any object at specifc location 
print len(bList)
bList.append(2021) # Append as name suggest always add the object at last position in List
print "B Final List : ", bList
 
