#Subarry
'''
arr = [1,2,3,4]
n = len(arr)
res = []
for i in range(n):
    for j in range(i+1,n+1):
        res.append(arr[i:j])
print(res)
'''
#Sub sequence
'''
def getsub(arr,ind=0,sub=None,res=None):
    if sub is None:
        sub = []
    if res is None:
        res = []
    if ind == len(arr):
        res.append(sub)
        return res
    getsub(arr,ind+1,sub,res)

    getsub(arr,ind+1,sub+[arr[ind]],res)

    return res
arr = [1,2,3,4]
mainres = getsub(arr)
print(mainres)
'''
#Problem - 1 [Longest Subarray with product == target ]
'''
arr = [1,2,3,4]
t = 6
n = len(arr)
res = []
for i in range(n):
    for j in range(i+1,n+1):
        res.append(arr[i:j])
print(res)
res1 = []
for arr in res:
    x = 1
    for i in arr:
        x = x * i
    if x == t:
        res1.append(arr)
print(res1)
mlen = 0
for i in res1:
    mlen = max(mlen,len(i))
for i in res1:
    if len(i) == mlen:
        print(i)
        break
'''
#Problem - 2 [Smallest Subarray with product == target ]
'''
arr = [1,2,3,4]
t = 6
n = len(arr)
res = []
for i in range(n):
    for j in range(i+1,n+1):
        res.append(arr[i:j])
print(res)
res1 = []
for arr in res:
    x = 1
    for i in arr:
        x = x * i
    if x == t:
        res1.append(arr)
print(res1)
mlen = n
for i in res1:
    mlen = min(mlen,len(i))
for i in res1:
    if len(i) == mlen:
        print(i)
        break
'''
#Problem - 3 [Largest Subarray with sum == target ]
'''
arr = [1,2,3,4]
t = 6
n = len(arr)
res = []
for i in range(n):
    for j in range(i+1,n+1):
        res.append(arr[i:j])
print(res)
res1 = []
for arr in res:
    x = 0
    for i in arr:
        x = x + i
    if x == t:
        res1.append(arr)
print(res1)
mlen = 0
for i in res1:
    mlen = max(mlen,len(i))
for i in res1:
    if len(i) == mlen:
        print(i)
        break
'''
#Problem - 4 [smallest Subarray with sum == target ]
'''
arr = [1,2,3,4]
t = 6
n = len(arr)
res = []
for i in range(n):
    for j in range(i+1,n+1):
        res.append(arr[i:j])
print(res)
res1 = []
for arr in res:
    x = 0
    for i in arr:
        x = x + i
    if x == t:
        res1.append(arr)
print(res1)
mlen = n
for i in res1:
    mlen = min(mlen,len(i))
for i in res1:
    if len(i) == mlen:
        print(i)
        break
'''
#Problem - 5 [Largest Subsequence with Product == target ]
'''
def getsub(arr,ind=0,sub=None,res=None):
    if sub is None:
        sub = []
    if res is None:
        res = []
    if ind == len(arr):
        res.append(sub)
        return res
    getsub(arr,ind+1,sub,res)

    getsub(arr,ind+1,sub+[arr[ind]],res)

    return res
arr = [1,2,3,4]
t = 6
res = getsub(arr)
print(res)
res1 = []
for arr in res:
    x = 1
    for i in arr:
        x = x * i
    if x == t:
        res1.append(arr)
print(res1)
mlen = 0
for i in res1:
    mlen = max(mlen,len(i))
for i in res1:
    if len(i) == mlen:
        print(i)
        break
'''
#Problem - 6 [smallest Subsequence with Product == target ]
'''
def getsub(arr,ind=0,sub=None,res=None):
    if sub is None:
        sub = []
    if res is None:
        res = []
    if ind == len(arr):
        res.append(sub)
        return res
    getsub(arr,ind+1,sub,res)

    getsub(arr,ind+1,sub+[arr[ind]],res)

    return res
arr = [1,2,3,4]
n = len(arr)
t = 6
res = getsub(arr)
print(res)
res1 = []
for arr in res:
    x = 1
    for i in arr:
        x = x * i
    if x == t:
        res1.append(arr)
print(res1)
mlen = n
for i in res1:
    mlen = min(mlen,len(i))
for i in res1:
    if len(i) == mlen:
        print(i)
        break
'''
#Problem - 7 [Largest Subsequence with sum == target ]
'''
def getsub(arr,ind=0,sub=None,res=None):
    if sub is None:
        sub = []
    if res is None:
        res = []
    if ind == len(arr):
        res.append(sub)
        return res
    getsub(arr,ind+1,sub,res)

    getsub(arr,ind+1,sub+[arr[ind]],res)

    return res
arr = [1,2,3,4]
t = 6
res = getsub(arr)
print(res)
res1 = []
for arr in res:
    x = 0
    for i in arr:
        x = x + i
    if x == t:
        res1.append(arr)
print(res1)
mlen = 0
for i in res1:
    mlen = max(mlen,len(i))
for i in res1:
    if len(i) == mlen:
        print(i)
        break
'''
#Problem - 8 [smallest Subsequence with sum == target ]
'''
def getsub(arr,ind=0,sub=None,res=None):
    if sub is None:
        sub = []
    if res is None:
        res = []
    if ind == len(arr):
        res.append(sub)
        return res
    getsub(arr,ind+1,sub,res)

    getsub(arr,ind+1,sub+[arr[ind]],res)

    return res
arr = [1,2,3,4]
n = len(arr)
t = 6
res = getsub(arr)
print(res)
res1 = []
for arr in res:
    x = 0
    for i in arr:
        x = x + i
    if x == t:
        res1.append(arr)
print(res1)
mlen = n
for i in res1:
    mlen = min(mlen,len(i))
for i in res1:
    if len(i) == mlen:
        print(i)
        break
'''
#Problem - 9
'''
arr = [1,2,3,4]
[24,12,8,6]
'''
#Approach - 1
'''
arr = [1,2,3,4]
n = len(arr)
res = []
for i in range(n):
    x = 1
    for j in range(n):
        if i != j:
            x = x * arr[j]
    res.append(x)
print(res)
'''
#Approach - 2
'''
arr = [1,2,3,4]
n = len(arr)
res = []
tp = 1
for i in arr:
    tp = tp * i
for i in arr:
    x = tp//i
    res.append(x)
print(res)
'''



