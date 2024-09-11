#Type Convertions
#Int - int => String,Float
'''
a = 10
b = str(a)
print(b,type(b))
c = float(a)
print(c,type(c))
'''
#float - flaot
'''
a = 10.456
b = int(a)
print(b,type(b))
c = str(a)
print(c,type(c))
'''
#String - str
'''
a = "10"
b = "10.456"
c = int(a)
print(c,type(c))
d = float(b)
print(d,type(d))
'''
#List - list
'''
a = [10,20,30,40,50]
x = str(a)
print(x,type(x))
print(x[5])
z = tuple(a)
print(z,type(z))
'''
#Tuple - tuple
'''
a = (1,2,3,4)
x = list(a)
print(x,type(x))
y = str(a)
print(a,type(a))
print(y[2])
'''
#Input Formatting
'''
x = input("Enter X value: ")
print(x,type(x))

y = int(input("Enter Y value: "))
print(y,type(y))
'''
#Creating Hetrogeneous values
#String
'''
a = input()
x,y = input().split()
x,y = input().split(",")
print(x)
print(y)
'''
#int
'''
x = int(input())
print(x)
x,y = map(int,input().split())
print(type(x))
print(type(y))
x,y = map(int,input().split(","))
print(x,type(x))
print(y,type(y))
'''
#float
'''
x = float(input())
print(x,type(x))
x,z = map(float,input().split())
print(x,type(x))
print(z,type(z))
'''
#complex
'''
x = complex(input())
print(x,type(x))
'''
#list
#String input values
'''
x = input().split()
print(x)
print(type(x))
x = input().split(",")
print(x)
print(type(x))
'''
#Integer input values
'''
x = list(map(int,input().split()))
print(x)
print(type(x))
x = list(map(int,input().split(",")))
print(x)
print(type(x))
n = int(input())
x = list(map(int,input().split()))[:n]
print(x)
'''
#Float input values
'''
x = list(map(float,input().split()))
print(type(x))
'''
#tuple
#sets
#frozensets
#boolean
#dictionary X





















