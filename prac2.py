'''
We import or include the file port in this code so that 
 we can use the function in port.py

'''
#to import the port.py the syntax is import file_name

import port

var1=int(input("Enter 1st integer number:"))
var2=int(input("Enter 2nd integer number:"))
var3=int(input("Enter 3rd integer number:"))
#file_name.function_name
port.compute(var1,var2,var3)
