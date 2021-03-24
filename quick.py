#!/usr/bin/python

def pretty(func):
    def inner ():
     print "I got Decorated"
     func()
    return inner

@pretty
def ordinary():
    print "I am Ordinary"
x=ordinary()
