#!/usr/bin/python

class Sample():

    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3
obj1 = Sample()
print dir(obj1)
