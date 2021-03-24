#!/usr/bin/python

A=['ACB','ACM','ABB','BLL']
A.insert(0,'hceTM')
B=[]
for i in A:
    i=i[::-1]
    B.append(i)
print "Now List content reversed :" ,B
B=B[::-1]  # B.reverse() --> reverse function can also be used directly here as mentioned
print "Complte Revesed list:",B

########## LIST COMPREHENSION ########
A.reverse()
C=[i[::-1] for i in A] 
print "Comprehension way ",C


