#!/usr/bin/python 
a=int(input("enter the number "))
sum=0
NUM=a
while a>0:
    ld=a%10
    sum=sum+ ld**3
    a //=10

    if (NUM==sum):
        print "Armstrong",sum,NUM
