#!/usr/bin/python
LST=[];y=1
x="This is Try ,perl=%s, java=%s, VB=%s, Su=%s"
for j in x.split(" "):
  y;xy="X"+str(y)
  x=j.replace("%s",xy)
  #x=j.replace("%d",xy)
  y=y+1
  #print "what left after replac",x
  LST.append(x)
  #print "Now j is ",str.join(x)
print "final is ",LST
str=" "
print "Now FINAL  ",str.join(LST)
