#!/usr/bin/python

def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

for item in my_gen():
    print(item)


my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
next(a)



#for i in a:
 #   print "values:",next(a)

