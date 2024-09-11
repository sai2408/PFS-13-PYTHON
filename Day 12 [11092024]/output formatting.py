#Problem - 1
'''
name = input("Enter Your name: ")
age = int(input("Enter Your Age: "))
height = float(input("Enter Your Height: "))
#Normal Method
print(name,"is",age,"years old. Height is",height)
#Modulo
print("%s is %d years old. Height is %f"%(name,age,height))
#F-format
print(f"{name} is {age} years old. Height is {height}")
#Dot-format
print("{} is {} years old. Height is {:.2f}".format(name,age,height))
'''
#Problem - 2
#Input
'''
Sai,Vardhan -> first_name and last_name
24-8-2000 -> date_of_birth [date,month,year]
5.7 -> height
'''
#Output:
'''
First name : Sai
Last name : vardhan
Birth Details
Date : 24
Month : August
Year : 2000
Height : 5.700
'''
#Source Code
'''
x = {1:"january",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
fn,ln = input("Enter Fname and Lname seperated with comma : ").split(",")
dd,mm,yyyy = map(int,input("Enter DOB [dd-mm-yyyy]: ").split("-"))
height = float(input("Enter your Height: "))
print("First name: {}".format(fn))
print("Last name: {}".format(ln))
print("Birth Details")
print("Date: {}".format(dd))
print("Month: {}".format(x[mm]))
print("Year : {}".format(yyyy))
print("Height : {:.3f}".format(height))
'''









    
