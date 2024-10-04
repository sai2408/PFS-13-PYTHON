#Recursive functions
#Problem - 1
#Approach - 1
'''
n = 10
while n>0:
    print(n)
    n = n - 1
'''
#Approach - 2
'''
def recr1(n):
    if n > 0:
        print(n)
    else:
        return
    recr1(n-1)
n = 10
recr1(n)
'''
#Problem - 2
#Approach - 1
'''
i = 1
while i <= 10:
    print(i)
    i = i + 1
'''
#Approach - 2
'''
def recr(n):
    if n <= 10:
        print(n)
    else:
        return
    recr(n+1)
n = 1
recr(n)
'''
#Problem - 4 [Series within a range]
#Approach - 1
'''
st = 10
end = 40
while st <= 40:
    print(st)
    st =st + 1
'''
#Appraoch - 2
'''
def recr(start,end):
    if start <= end:
        print(start)
    else:
        return
    recr(start+1,end)
st = 10
end = 40
recr(st,end)
'''
#Problem - 5 [ Factorial ]
'''
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
x = fact(5)
print(x)
'''
#Problem - 6
#Approach - 1
'''
def sample(n):
    s = 0
    for i in range(1,n+1):
        if n%i == 0:
            s  = s + 1
    if s == 2:
        return True
    else:
        return False
x = 0
def recr(st,end):
    global x
    if st <= end:
        if sample(st):
            x = x + st
        recr(st+1,end)
    else:
        print(x)
        return 
st = 11
end = 20
recr(st,end)
'''


    
    
















