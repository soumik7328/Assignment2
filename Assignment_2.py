#Assignment-2: Python Basics
#1. Write a python script to add comments and print “Learning Python” on screen.
#print("Learning python")
print("Learning python")
#2. Write a python script to add multi line comments and print values of four variables,each in a new line. Variable contains any values.
'''a=2
b=3
c=4
d=5
print(a,b,c,d, sep="\n")'''
#3. Write a python script to print types of variables. Create 5 variables each of them
#containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
a=35
b=True
c="MySirG"
d=5.46
e=3+4j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
#4. Write a python script to print the id of two variables containing the same integer values.
a=16
b=16
print(id(a))
print(id(b))

#5. Create four variables in a Python script and assign values of different data types to
#them. Write a Python script to print value, its type and id of each variable
a=35
c="MySirG"
d=5.46
e=3+4j
print("value a=%d  c=%s  d=%f "%(a,c,d), "e=",e)
print(type(a))
print(type(c))
print(type(d))
print(type(e))
print(id(a))
print(id(c))
print(id(d))
print(id(e))

#6. Write a python script to print all the keywords
import keyword
print(keyword.kwlist)
#7. On Python shell use help() function and display the list of keywords 
#>>> open IDLE and type help("keywords")
#8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some value to it. Write a python script to import A1 module in A0 and print value of the variable created in A0.py

#9. Name the keywords, used as data in the Python script.
#ans:- False, None, True
#10. Write a python script to display the current date and time. First create variables to
#store date and time, then display date and time in proper format
from datetime import datetime
a=datetime.now()
print("Today's date and present time is ",a)

