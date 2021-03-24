#!/usr/bin/python 
key_value ={}     
# Initialize value  
key_value['2'] = 56       
key_value['1'] = 2 
key_value['5'] = 12 
key_value['4'] = 24
key_value['6'] = 18      
key_value['3']= 323 
   
for i in sorted (key_value.keys()): 
    print "Sorted by Key: ",i,key_value[i]
    
print "Sorted by value: ",sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])) 


  

