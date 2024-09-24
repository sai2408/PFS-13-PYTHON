#Pattern - 1
#Approach - 1 [For in  For]
'''
n = int(input("enter a number: "))
for i in range(n):
    for j in range(n):
        print(f"*",end=" ")
    print()
'''
#Approach - 2 [For in while]
'''
n = int(input("enter a nuber: "))
x = n
while n>0:
    for i in range(x):
        print("*",end= " ")
    print()
    n = n - 1
'''
#Approach - 3 [While in While]
'''
n= int(input("enter a number: "))
x = n
while x > 0:
    y = n
    while y > 0:
        print("*",end= " ")
        y = y - 1
    print()
    x = x - 1
'''
#Appoach - 4 [While in For]
'''
n = int(input("Enter a number"))
x = n
while n>0:
    for i in range(x):
        print("*",end=" ")
    n = n -1
    print()
'''
#Pattern - 2
'''
n = int(input("enter a number: "))
for i in range(n):
    for j in range(n):
        if i>=j:
            print("*",end=" ")
    print()
'''
#Pattern - 3
'''
n = int(input("enter a number: "))
for i in range(n):
    for j in range(n):
        if j%2 == 0:
            print("*",end= " ")
        else:
            print("@",end=" ")
    print()
'''
#Pattern - 3
'''
n = int(input("enter a number: "))
for i in range(n):
    if i%2 == 0:
        for j in range(n):
            print("*",end=" ")
    else:
        for j in range(n):
            print("#",end=" ")
    print()
'''
#pattern - 4
'''
n = int(input("enter a number: "))
for i in range(n):
    for j in range(n):
        if (i+j)%2 == 0:
            print("#",end=" ")
        else:
            print("*",end=" ")
    print()
'''
#Pattern - 5
'''
n = int(input("enter a number: "))
for i in range(n):
    for j in range(n):
        if i==j:
            print("*",end=" ")
        elif i<j:
            print("@",end=" ")
        else:
            print("#",end=" ")
    print()
'''
#Pattern - 6 [Halo Pattenrs]
'''
n = int(input("enter a number: "))
for i in range(n):
    for j in range(n):
        if i==0 or i == n-1 or j == 0 or j==n-1:
            print("*",end=" ")
        else:
            print(" " ,end= " ")
    print()
'''
#Assignment


















        
