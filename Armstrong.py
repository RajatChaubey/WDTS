#!/usr/bin/python
for num in range(100,1000):
 sum=0 
 temp = num
 while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
 if num == sum:
       print(num,"is an Armstrong number")

