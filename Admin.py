#!/usr/bin/python
from DbController import DbController

obj = DbController()

print ("Admin Interface")
print ("\n1. Add\n2. Remove")
ch = int(raw_input("Enter the input:"))
if ch == 1:
   print ("Adding")
   obj.Read_Data()
   
elif ch == 2:
   name= str(raw_input("Enter the name:"))
   obj.Remove_Data(name)
   
else:
   print ("Invalid request. Press R to retry")
