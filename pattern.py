#!/usr/bin/python

def pyramid(n):
  for row in range(n):
    for space in range(n-row):
      print " ",
    for star in range(row):
      print '*',
    for star in range(row+1):
      print '*',
    print


pyramid(5)

