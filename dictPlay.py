# creating a new dictionary 
my_dict ={"JAVA":100, "Python":112, "PERL":11} 
# list out keys and values separately 
key_list = list(my_dict.keys()) 
val_list = list(my_dict.values()) 

#print(key_list[val_list.index(100)]) # prints JAVA 

for i in val_list:
    print(key_list[val_list.index(i)])

