#!/usr/bin/python
x = int(raw_input("How many terms? "))
n1, n2 = 0, 1
count = 0
print("Fibonacci sequence:")
while count < x:
       print(n1)
       temp = n1 + n2
       n1 = n2
       n2 = temp
       count += 1

