#!/usr/bin/python


file = open('Alarms.csv', 'r') 
# This will print every line one by one in the file 
for each in file: 
    print (each) 

file = open("ALARM_DATA.txt", "r")  
print file.read() 

print "# This will just print the first line of file \n"""
file1 = open("ALARM_DATA.txt", "r")
print file1.readline() 

print "\n ## This will print all lines in a List way  \n "
file2 = open("ALARM_DATA.txt", "r")
lst=file2.readlines()
print "Print to chk the list ", lst  # You can print entire list --> lst or any specific element like lst[5]



