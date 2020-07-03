#!/usr/bin/python
#import ReadCMT
import subprocess
import os
cmd = 'ls -lrt *CMTBuilder*'
#os.system(cmd)


out = subprocess.Popen('ls -lrt *CMTBuilder*', shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)


#out = subprocess.Popen(['ls','-lrt','*CMTBuilder*'],           stdout=subprocess.PIPE,            stderr=subprocess.STDOUT)

stdout,stderr = out.communicate()
print(stdout)
print (stdout.split()[8])
#v,w=ReadCMT.CMTvalues()

#print "MODULE TEST this are values ",v,w

