#!/usr/bin/python 

# Use of property() function 

class Geeks: 
	def __init__(self,age): 
		self.age = age
	
	# function to get value of _age 
	def get_age(self): 
		print "getter method called",self.age
		return self._age 
	
	# function to set value of _age 
	def set_age(self,age): 
		print "setter method called"
		self._age = a 

	# function to delete _age attribute 
	def del_age(self): 
		del self._age 
	
	age = property(get_age, set_age, del_age) 

mark = Geeks(50) 

print mark.age , "This is coming from Getter only"

mark.age=70
print mark.age, "This happened after Re-Setting via Setter"


