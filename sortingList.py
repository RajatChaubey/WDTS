#!/usr/bin/python
List=[(4,6),(8,3),(4,6),(7,8),(3,5)]

List.sort(key=lambda x: x[0]) 
print "Sorting done based on first element of tuple in List",List
# that is index[0]

List.sort(key=lambda x: x[1])
print "Sorting done based on Second element of tuple in List",List 
# that is index[1]
