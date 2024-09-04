#Dictionaries
#Creation
#Homogeneous
'''
d = {}
print(d)
print(type(d))
d = {"name":"Sai",10:100,23.45 :
     "abc"}
print(d)
print(type(d))
'''
#Hetrogeneous X
#Accessing
#Indexing
'''
d = {10:100,20:200,30:300}
print(d[10])
print(d[20])
'''
#Looping X
#Methods
'''
d = {1:100,2:200,3:300,4:400}
#get()
print(d.get(1))
print(d.get(100))
#copy()
x = d.copy()
print(x)
#keys()
print(d.keys())
#values()
print(d.values())
#items()
print(d.items())
'''
#Updation
'''
#Indexing
d = {1:10,2:200,3:30,4:40}
d[2] = "abc"
print(d)
#methods
#update()
d.update({2:20,5:50})
print(d)
#fromkeys()
x = {1,5,2,3,4}
z = dict.fromkeys(x,30)
print(z)
'''
#Deletion
'''
#indexing
d = {1:10,2:20,3:35,4:40}
del d[3]
print(d)
#methods
#pop()
d1 = {1:10,2:20,3:30,4:40,5:50}
d1.pop(2)
print(d1)
#popitems()
d1.popitem()
print(d1)
#clear()
d1.clear()
print(d1)
'''
#Nested Dictionaries
'''
emp1 = {'name':'sai','salary':60000,'dob':[24,8,1997]}
print(emp1['name'])
print(emp1['dob'][1])
'''
    















