#Problem - 1
#Approach - 1
'''
s = input()
x = input()
res = 0
for i in range(len(s)):
    if s[i] == x:
        res = res + 1
print(res)
'''
#Approach - 2
'''
s = input()
x = input()
res = 0
for i in s:
    if i == x:
        res = res + 1
print(res)
'''
#Approach - 3
'''
s = input()
x = input()
res = s.count(x)
print(res)
'''
#Problem - 2
#Approach - 1
'''
s = input()
v = "aeiouAEIOU"
for i in range(len(s)):
    if s[i] not in v:
        print("No")
        break
else:
    print("Yes")
'''
#Approach - 2
'''
s = input()
v = "aeiouAEIOU"
for i in s:
    if i not in v:
        print("No")
        break
else:
    print("Yes")
'''
#Approach - 3
'''
s = input()
v = "aeiouAEIOU"
vc = 0
for i in s:
    if i in v:
        vc = vc + 1
if vc == len(s):
    print("Yes")
else:
    print("No")
'''
#APproach - 4
'''
s = input()
v = "aeiouAEIOU"
cc = 0
for i in s:
    if i not in v:
        cc = cc + 1
if cc > 0:
    print("No")
else:
    print("Yes")
'''
#Problem - 3
#Appraoch - 1
'''
s = input()
d = "0123456789"
for i in range(len(s)):
    if s[i] not in d:
        print("No")
        break
else:
    print("Yes")
'''
#Appraoch - 2
'''
s = input()
d = "0123456789"
for i in s:
    if i not in d:
        print("No")
        break
else:
    print("Yes")
'''
#Appraoch - 3
'''
s = input()
dc = 0
d = "1234567890"
for i in s:
    if i in d:
        dc = dc + 1
if dc == len(s):
    print("Yes")
else:
    print("No")
'''
#Approach - 4
'''
s = input()
if s.isdigit():
    print("Yes")
else:
    print("No")
'''
#Problem - 4
'''
s = input()
res = ""
c = 1
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        c = c + 1
    else:
        res = res + s[i-1]
        res = res + str(c)
        c = 1
res = res + s[-1]
res = res + str(c)
print(res)
'''































