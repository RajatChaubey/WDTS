#!/usr/bin/python
try:
  fh=open("TEST_FILE","r")
  fh1=open("TEST_FILE1","w")
  for i in fh:
    fh1.write(i.replace("is","#WAS#"))
  fh.close
  fh1.close
except IOError:
  print "File not found.Take corrective action"

