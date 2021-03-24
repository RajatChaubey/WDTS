#!/usr/bin/python
# function that filters vowels 
def fun (variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        print "",variable + "Vowel" 
    else: 
        print variable,"is not a vowel"
  
  
# sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
  
# using filter function 
filtered = filter(fun, sequence) 
  
print('The filtered letters are:') 
for s in filtered: 
    print(s)
