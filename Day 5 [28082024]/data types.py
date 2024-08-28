#Numeric types
'''
#Int
a = 10
print(a)
print(type(a))
x1 = 10
x2 = 20
print(x1+x2)
#Float
b = 10.3456
print(b)
print(type(b))
k1 = 10.56
k2 = 20.12
print(k1+k2)
#complex
c = 3 + 4j
print(c)
print(type(c))
c1 = 2 + 4j
c2 = 4 + 2j
print(c1+c2)
'''
#Lists
#Creation
#Homogeneoues
'''
a = []
print(a)
print(type(a))
a = [10,20,"a","b",34]
print(a)
print(type(a))
'''
#Hetrogeneous
'''
I/O Statements
'''
#Accessing
#Indexing
'''
a = [10,20,30,40,50,60]
#Positve indexing
print(a[2])
#Negetive Indexing
print(a[-3])
'''
#Methods
'''
a = [10,20,30,40,50,60,20,90,20]
x = a.index(40)
print(x)
y = a.count(20)
print(y)
z = a.copy()
print(z)
#Deep copy
a = [10,20,30,40]
b = a.copy()
print(a)
print(b)
b[2] = 300
print(a)
print(b)
#Shallow Copy
a = [10,20,30,40]
b = a
print(a)
print(b)
b[2] = 300
print(a)
print(b)
'''
#Looping
'''
Discussed Later
'''
#Slicing
'''
a = [10,20,30,40,50,60,70,80,90]
print(a[::])
print(a[:])
print(a[::1])
print(a[:1])
print(a[3:7:2])
print(a[::-1])
'''
#Insertion
'''
a = [10,20,30]
print(a)
#append()
a.append(40)
print(a)
#Extend()
a.extend([30,55,67])
print(a)
#insert()
a.insert(3,35)
print(a)
a.insert(0,5)
print(a)
'''
#Deletion
'''
a = [10,20,30,40,50,20,70]
print(a)
#remove()
a.remove(40)
print(a)
a.remove(20)
print(a)
#pop()
a.pop()
print(a)
a.pop(2)
print(a)
#clear()
a.clear()
print(a)
'''
#Updation
#Built in Functions
#External Operations
















