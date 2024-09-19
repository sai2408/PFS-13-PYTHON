#Problem - 1
#Approach - 1 [For loop]
'''
for i in range(1,51):
    print(i)
'''
#Appraoch - 2 [While loop]
'''
n = 1
while n <= 50:
    print(n)
    n = n + 1
'''
#Problem - 2
#Approach - 1
'''
for i in range(2,11,2):
    print(i)
'''
#Approach - 2
'''
n = 2
while n < 11:
    print(n)
    n = n + 2
'''
#Approach- 3
'''
for i in range(1,11):
    if i%2==0:
        print(i)
'''
#Approach - 4
'''
n = 1
while n<11:
    if n%2==0:
        print(n)
    n = n + 1
'''
#Problem - 3
#Approach - 1
'''
start = int(input("enter start value: "))
end = int(input("enter end value: "))
es = 0
os = 0
for i in range(start,end+1):
    if i%2==0:
        es = es + i
    else:
        os = os + i
res = (es+os)/2
print(res)
'''
#Approach - 2
'''
start = int(input("enter start value: "))
end = int(input("enter end value: "))
es = 0
os = 0
while start < end+1:
    if start%2 == 0:
        es = es + start
    else:
        os = os + start
    start = start + 1
res = (es+os)/2
print(res)
'''
#Approach - 3
'''
start = int(input("enter start value: "))
end = int(input("enter end value: "))
es = []
os = []
for i in range(start,end+1):
    if i%2 == 0:
        es.append(i)
    else:
        os.append(i)
res = (sum(es) + sum(os))/2
print(res)
'''
#Approach - 4
'''
start = int(input("enter start value: "))
end = int(input("enter end value: "))
es = []
os = []
while start < end+1:
    if start%2 == 0:
        es.append(start)
    else:
        os.append(start)
    start = start + 1
res = (sum(es) + sum(os))/2
print(res)
'''
#Problem - 4
'''
t = int(input())
for i in range(t):
    x = int(input())
    if x > 98:
        print("Yes")
    else:
        print("No")
'''
#Problem - 5
#Approach - 1
'''
t= int(input())
for i in range(t):
    x = int(input())
    if x>=1 and x<=4:
        print("Yes")
    else:
        print("No")
'''
#Approach - 2
'''
t = int(input())
while t > 0:
    x = int(input())
    if  x>=1 and x<=4:
        print("Yes")
    else:
        print("No")
    t = t - 1
'''
#Problem - 6
#Approach - 1
'''
start = int(input())
end= int(input())
x = []
for i in range(start,end+1):
    if i%4 == 0:
        x.append(i)
print(x)
'''
#Approach - 2
'''
start = int(input())
end= int(input())
x = []
while start <= end:
    if start%4 == 0:
        x.append(start)
    start = start + 1
print(x)
'''
#Approach - 3 [list comprehension]
#list = [<output variable> <Sequence> <condition>]
'''
start = int(input())
end= int(input())
x = [i for i in range(start,end+1) if i%4==0]
print(x)
'''
#Problem - 7
'''
x = [12,45,23,78]
#With range
for i in range(len(x)):
    print(x[i])
#without range
for i in x:
    print(i)
'''
#Problem - 7
#Approch - 1
'''
t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))[:n]
    b = list(map(int,input().split()))[:n]
    tc = 0
    for i in range(n):
        if a[i] >= x:
            tc = tc + b[i]
    print(tc)
'''
#Approaach- 2
'''
t = int(input())
for i in range(t):
    d = {}
    n,x = map(int,input().split())
    a = list(map(int,input().split()))[:n]
    b = list(map(int,input().split()))[:n]
    for i in range(n):
        d[a[i]] = b[i]
    tc = 0
    for key in d:
        if key >= x:
            tc = tc + d[key]
    print(tc)
'''
#Problem - 8
'''
d = {}
n = int(input())
for i in range(n):
    key,value = map(int,input().split())
    d[key] = value
print(d)
'''







    









        
    

    
    

















    
