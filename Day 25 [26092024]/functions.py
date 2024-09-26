#Built in functions
'''
print(abs(100))
print(abs(-100))
print(ord("d"))
x = chr(100)
print(x)
x = "10+20-10"
print(eval(x))
y = "abs((10-20)+(10-21))"
print(eval(y))
print(bin(10))
print(oct(10))
print(hex(10))
print(sum([10,20,30]))
y = 20
print(id(y))
'''
#Used defined functions
#WPWR
'''
def mno(x,y):
    v1 = x - y
    v2 = x + y
    v3 = x * y
    return v1,v2,v3
t = int(input())
for i in range(t):
    a = int(input("enter a number: "))
    b = int(input("Enter a number: "))
    r1,r2,r3 = mno(a,b)
    print(r1)
    print(r2)
    print(r3)
'''
#WPWOR
'''
def mno(x,y):
    v1 = x - y
    v2 = x + y
    v3 = x * y
    print(v1)
    print(v2)
    print(v3)
t = int(input())
for i in range(t):
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    mno(a,b)
'''
#WOPWR
'''
def mno():
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    v1 = a - b
    v2 = a + b
    v3 = a * b
    return v1,v2,v3
t = int(input())
for i in range(t):
    r1,r2,r3 = mno()
    print(r1)
    print(r2)
    print(r3)
'''
#WOPWOR
'''
def mno():
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    v1 = a - b
    v2 = a  + b
    v3 = a * b
    print(v1)
    print(v2)
    print(v3)
t = int(input())
for i in range(t):
    mno()
'''


















