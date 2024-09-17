#Problem - 1
#Approach - 1
'''
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
print(f"{lname}, {fname}")
'''
#Approach- 2
'''
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
res = lname+", "+fname
print(res)
'''
#Problem - 2
#Approach - 1
'''
name = input("Enter your full name: ")
x = name.title()
print(f"Hello, {x}!")
'''
#Approach - 2
'''
name = input("Enter your full name: ")
x = name.title()
res = "Hello, "+x+"!"
print(res)
'''
#Problem - 3
'''
x = float(input("Enter a floating-point number: "))
print("{:.2f}".format(x))
'''
#Problem - 4
#Approach - 1
'''
n1 = int(input("Enter an integer: "))
n2 = float(input("Enter a float: "))
n3 = input("Enter a string: ")
print(f"{n1}, {n2}, {n3}")
'''
#Appraoch - 2
'''
n1,n2,n3 = input().split(",")
n1 =  int(n1)
n2 = float(n2)
print(f"{n1}, {n2}, {n3}")
'''
#Problem - 5
#Approach -1
'''
year = int(input("Enter your birth year: "))
age = 2024-year
print(f"You are {age} years old.")
'''
#Approach - 2
'''
year = int(input("Enter your birth year: "))
print(f"You are {2024-year} years old.")
'''
#Problem - 6
'''
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print(f"The numbers your entered are {n1} and {n2}.")
'''
#Problem - 7
'''
name = input("Enter the product name: ")
price = float(input("Enter the price: "))
print(f"Product: {name}")
print("Price:  {:.2f}".format(price))
'''
#Problem - 8
#Approach - 1
'''
string = input("Enter a sentence: ")
print("Your sentence:",string)
r1 = len(string)
r2 = string.count(" ")
print(f"Character count (excluding spaces): {r1-r2}")
'''
#Approach - 2
'''
string = input("Enter a sentence: ")
print("Your sentence:",string)
x = string.split()
r1 = len(string)
r2 = len(x)-1
print(f"Character count (excluding spaces): {r1-r2}")
'''
#Approach - 3
'''
string = input("Enter a sentence: ")
print("Your sentence:",string)
x = string.replace(" ","")
print(f"Character count (excluding spaces): {len(x)}")
'''
