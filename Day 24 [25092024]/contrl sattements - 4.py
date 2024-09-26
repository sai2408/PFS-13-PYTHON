#Problem - 1
'''
n => 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
'''
#Appraoch - 1 [With const]
'''
n = int(input("Enter a number: "))
for i in range(n):
    c = 1
    for j in range(n):
        print(f"{c}",end=" ")
        c = c + 1
    print()
'''
#Appraoch - 2 [without const]
'''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        print(f"{j+1}",end=" ")
    print()
'''
#Problem - 2
'''
n => 4
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
'''
#Approach - 1 [with const]
'''
n = int(input("enter a number: "))
c = 1
for i in range(n):
    for j in range(n):
        print(f"{c}",end=" ")
    print()
    c = c + 1
'''
#approach - 2 [without const]
'''
n = int(input("enter a number: "))
for i in range(n):
    for j in range(n):
        print(f"{i+1}",end=" ")
    print()
'''
#Problem - 3
'''
n => 4
1
1 2
1 2 3
1 2 3 4
'''
#Approach - 1 [With Const]
'''
n = int(input("enter a number: "))
for i in range(n):
    c = 1
    for j in range(n):
        if i>=j:
            print(f"{c}",end=" ")
        else:
            print(" ",end=" ")
        c = c + 1
    print()
'''
#Approach - 2 [Without const]
'''
n = int(input("enter a number: "))
for i in range(n):
    for j in range(n):
        if i>=j:
            print(f"{j+1}",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#Problem - 3
'''
n => 4
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''
#Approach - 1
'''
n = int(input("enter a number: "))
x = n
for i in range(n):
    c = x
    for j in range(n):
        if i>=j:
            print(f"{c}",end=" ")
        else:
            print(" ",end=" ")
        c = c - 1
    print()
'''
#Combination of numeric and symbolic patterns
#Problem - 1 [Incomplete ]
'''
n => 5
1
# #
2 3 4
# # # #
5 6 7 8 9
n => 4
1
# #
2 3 4
# # # #
'''
#Approach
'''
n = int(input("enter a number: "))
c = 1
for i in range(n):
    if i%2==0:
        for j in range(n):
            if i >= j:
                print(f"{c}",end=" ")
                c = c + 1
            else:
                print(" ",end=" ")
    else:
        for j in range(n):
            if i >= j:
                print("#",end=" ")
            else:
                print(" ",end=" ")
    print()
'''
#Problem - 2
'''
n => 5
#
5 4
# # #
3 2 1 0
# # # # #
n => 4
#
4 3
# # #
2 1 0 -1
'''
#Approach
'''
n = int(input("enter a number: "))
c = n
for i in range(n):
    if i%2 == 0:
        for j in range(n):
            if i>=j:
                print("#",end=" ")
            else:
                print(" ",end= " ")
    else:
        for j in range(n):
            if i>=j:
                print(f"{c}",end=" ")
                c = c - 1
            else:
                print(" ",end= " ")
    print()
'''
#Problem - 3
'''
n => 5
# # # # #
  1 2 3 4
    # # #
      5 6
        #
'''
#Matrix Problems [Nested Lists] => NL + NCS
#Problem - 1 [NXN]
'''
n = int(input())
matrix = []
for i in range(n):
    x = list(map(int,input().split()))[:n]
    matrix.append(x)
print(matrix)
'''
#Problem - 2 [NXM]
'''
n = int(input("Enter no of rows: "))
m = int(input("Enter no of cols: "))
matrix = []
for i in range(n):
    x = list(map(int,input().split()))[:m]
    matrix.append(x)
print(matrix)
'''
#Problem - 3 [Transpose]
'''
n = int(input("enter n value: "))
mat = []
for i in range(n):
    x = list(map(int,input().split()))
    mat.append(x)
res = []
for i in range(n):
    x = []
    for j in range(n):
        x.append(0)
    res.append(x)
for i in range(n):
    for j in range(n):
        res[i][j] = mat[j][i]
for i in mat:
    print(*i)
for i in res:
    print(*i)
'''
#Assignment
n = int(input("enter a number: "))
c = 9
for i in range(n):
    for j in range(n):
        if i == j:
            print(f"{c}",end=" ")
            c = c - 1
        else:
            print(f"{j+1}",end=" ")
    print()








    














    




















































































    
