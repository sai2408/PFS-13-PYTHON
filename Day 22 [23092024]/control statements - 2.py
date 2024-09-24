#Problem - 1 [ Prime Number ]
#Approach - 1
'''
n = int(input("Enter a number: "))
fc = 0
for i in range(1,n+1):
    if n%i == 0:
        fc = fc + 1
if fc > 2:
    print("Not a Prime number")
elif fc == 1:
    print("Neither Prime not Composite Number")
else:
    print("Prime Number")
'''
#Appraoch - 2
'''
n = int(input("Enter a number: "))
fc = 0
for i in range(2,n//2):
    if n%i == 0:
        fc = fc + 1
if fc > 1:
    print("Not a Prime number")
elif fc == 0:
    print("Neither Prime not Composite Number")
else:
    print("Prime Number")
'''
#Approach - 3
'''
n = int(input("Enter a number: "))
x = True
for i in range(2,n//2):
    if n%i == 0:
        x = False
        break
if x==True:
    print("Prime number")
else:
    print("Not a Prime Number")
'''
#Problem - 2 [Reverse of the number]
#Approach - 1
'''
n = int(input("Enter Number: "))
res = 0
if n >= 0:
    while n>0:
        r = n%10
        res = (res*10) + r
        n = n // 10
else:
    n = -1 * n
    while n>0:
        r = n%10
        res = (res*10) + r
        n = n // 10
    res = res * -1
print(res)
'''
#Appraoch - 2
'''
x = int(input())
if x > 0:
    x = str(x)
    x = x[::-1]
    print(x)
else:
    x = -1 * x
    x = str(x)
    x = x[::-1]
    x = "-" + x
    print(x)
'''
#Approach - 3
'''
n = int(input())
if n > 0:
    n = str(n)
    n = n[::-1]
    print(n)
else:
    n = abs(n)
    n = str(n)
    n = n [::-1]
    n = "-" + n
    print(n)
'''
#Problem - 4 [Factorial]
#Appraoch - 1
'''
n = int(input())
res = 1
for i in range(1,n+1):
    res = res * i
print(res)
'''
#Approach - 2
'''
n = int(input())
res = 1
while n > 0:
    res = res * n
    n = n - 1
print(res)
'''
















