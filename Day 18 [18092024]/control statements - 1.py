#Problem - 1
'''
a = [10,20,30,40,50]
'''
#Appraoch - 1 [ For using Range ]
'''
n = len(a)
for i in range(n):
    print(a[i])
for i in range(n):
    print(a[i],end= " ")
print()
for i in range(n):
    print(a[i],end=",")
'''
#Approch - 2 [ for without using range ]
'''
for i in a:
    print(i)
for i in a:
    print(i,end=" ")
print()
for i in a:
    print(i,end=",")
'''
#Approach - 3 [Keywargs]
'''
print(*a)
print(*a,sep=" " )
print(*a,sep=",")
'''
#Problem - 2
'''
a = list(map(int,input().split()))[:99]
for i in range(1,101):
    if i not in a:
        print(i)
        break
'''







        

