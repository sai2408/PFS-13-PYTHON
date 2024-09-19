#Problem - 1
'''
a,b = map(int,input().split())
if a>b:
    print("a > b")
elif a<b:
    print("a < b")
else:
    print("a == b")
'''
#Problem - 2
'''
a,b,c = map(int,input().split())
if ((a+b>c) and (b+c>a) and (c+a>b)):
    print("Yes")
else:
    print("No")
'''
#Problem - 3
'''
w = int(input())
if ((w>2) and (w%2==0)):
    print("Yes")
else:
    print("No")
'''
#Problem - 4
'''
x,y = map(int,input().split())
m = y // 2
n = x - y
print(m+n)
'''
#Problem - 5
'''
x = int(input())
if (x%2==0):
    print(x+2)
else:
    print(x+1)
'''
#Problem - 6
'''
n = int(input())
if n > 0:
    x = "3" + str(n) + "3"
    print(x)
else:
    n = n * -1
    x = "3" + str(n) + "3"
    print(-1 * int(x))
'''




























