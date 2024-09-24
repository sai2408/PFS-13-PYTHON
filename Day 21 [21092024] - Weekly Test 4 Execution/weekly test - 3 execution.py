#Problem - 1
#Approach - 1
'''
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if (a+b)%2!=0 or (b+c)%2!=0 or (c+a)%2!=0:
        print("Yes")
    else:
        print("No")
'''
#Problem - 2
#Approach - 1
'''
a=int(input())
for i in range(a):
    x=int(input())
    if x>=30:
        print("yes")
    else:
        print("No")
'''
#Approach - 2
'''
n = int(input())
for i in range(a):
    x=int(input())
    if x<30:
        print("No")
    else:
        print("Yes")
'''
#Approach - 3
'''
n=int(input())
i=0
while i<n:
    x=int(input())
    if(x>=30):
        print("Yes")
    else:
        print("No")
    i=i+1
'''
#Approach - 4
'''
n = int(input())
for i in range(n):
    x = input()
    if int(x)>=30:
        print("Yes")
    else:
        print("No")
'''
#Problem - 3
#Approach - 1
'''
a,b,c,x=map(int,input().split())
if(x==a) or (x==b) or (x==c):
    print("Yes")
else:
    print("No")
'''
#Approach - 2
'''
a,b,c,d = map(int,input().split())
x = []
x.append(a)
x.append(b)
x.append(c)
if d in  x:
    print("Yes")
else:
    print("No")
'''
#Approach - 3
'''
x =  list(map(int,input().split()))
a = x.pop()
if a in x:
    print("Yes")
else:
    print("No")
'''
#Approach - 4
'''
a,b,c,d = map(int,input().split())
if d in [a,b,c]:
    print("Yes")
else:
    print("No")
''' 
#Problem - 4
#Approach - 1
'''
n=int(input())
i=1
while i<=10:
    print(f"{n} x {i}={n*i}")
    i+=1
'''
#Approach - 2
'''
n=int(input())
for i in range(1,11):
    print(f'{n} * {i} = {n*i}')
'''



