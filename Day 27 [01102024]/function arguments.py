#Default arguments
'''
def abc(x=0,y=0,z=0):
    c = x + y + z
    print(c)
abc()
abc(10)
abc(10,20)
abc(10,20,30)
'''
#Variable number of argumnets
'''
def abc(*sai):
    x = 0
    for i in sai:
        x = x  + i
    print(x)
abc()
abc(10)
abc(10,20)
abc(10,20,30)
abc(10,20,30,40)
'''
#Required Argumnets
'''
def abc(a,b,c):
    c = a + b + c
    print(c)
abc(10,20,30)
'''
#Keyword Argumnets
'''
def details(name,age):
    print("Name:",name)
    print("Age:",age)
details("sai",56)
details(56,"sai")
details(name="sai",age=56)
details(age=56,name="sai")
'''
#Example - 1
'''
a = 10
def hello():
    a = 20
    print(a)
print(a)
hello()
'''
#Example - 2
'''
a = 10
def hello():
    b = 20
    print(a)
print(a)
hello()
'''
#Example - 3
'''
a = 10
def hello():
    a = 45
    print(a)
hello()
'''
#Example - 4
'''
a = 10
def hello():
    global a
    a = a + 20
    print(a)
hello()
''''























