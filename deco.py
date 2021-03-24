#!/usr/bin/python
def star(f):
    def inner(*args):
        print("*" * 30)
        f(*args)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args):
        print("%" * 30)
        func(*args)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")
