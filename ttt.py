#!/usr/bin/python
nums=[1,2,5,10,3,4,9,24]
for i in nums:
          print "Now i is - ",i
          if i<5:
              nums.remove(i)
              print "Now left arrray after remove is ",nums
print nums
