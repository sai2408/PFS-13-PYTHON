#Sets
#creation
'''
#Homogeneous
s1 = set()
print(s1)
print(type(s1))
s2 = set([1,2,3,4,2,3])
print(s2)
print(type(s2))
s3 = {1,2,3,4,2,3}
print(s3)
print(type(s3))
#Hetrogeneous X
'''
#Accessing
#Looping X
#Methods
#copy()
''''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1)
print(s2)
s3 = s1.copy()
print(s3)
print(s1)
print(s2)
'''
#union()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = s1.union(s2)
s4 = s1 | s2
print(s3)
print(s4)
'''
#intersection()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = s1.intersection(s2)
s4 = s1 & s2
s5 = s2.intersection(s1)
s6 = s2 & s1
print(s3)
print(s4)
print(s5)
print(s6)
'''
#difference()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1)
print(s2)
s3 = s1.difference(s2)
s4 = s1 - s2
s5 = s2.difference(s1)
s6 = s2 - s1
print(s3)
print(s4)
print(s5)
print(s6)
'''
#symmetric_difference()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1)
print(s2)
s3 = s1.symmetric_difference(s2)
s4 = s1 ^ s2
print(s3)
print(s4)
s5 = s2.symmetric_difference(s1)
s6 = s2 ^ s1
print(s5)
print(s6)
'''
#isdisjoint()
'''
s1 = {1,2,13,14}
s2 = {3,4,5,6}
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))
'''
#issubset()
'''
s1 = {1,2}
s2 = {1,2,3,4}
print(s1.issubset(s2))
print(s2.issubset(s1))
'''
#issuperset()
'''
s1 = {1,2}
s2 = {1,2,3,4}
print(s1.issuperset(s2))
print(s2.issuperset(s1))
'''
#insertion
'''
#Methods
#add()
s1 = {1,2,3,4}
print(s1)
s1.add(5)
print(s1)
#update()
s1 = {1,2,3,4}
print(s1)
s1.update({5,6})
print(s1)
'''
#updation
#Methods
#update()
'''
s1 = {1,2,3,4}
print(s1)
s1.update({4,5})
print(s1)
'''
#intersection_update()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1)
print(s2)
s2.intersection_update(s1)
print(s1)
print(s2)
'''
#difference_update()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1)
print(s2)
s2.difference_update(s1)
print(s1)
print(s2)
'''
#symmetric_difference_update()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1)
print(s2)
s2.symmetric_difference_update(s1)
print(s1)
print(s2)
'''
#deletion
#remove()
'''
s1 = {1,2,3,4,5}
print(s1)
s1.remove(3)
print(s1)
'''
#discard()
'''
s1 = {1,2,3,4,5}
print(s1)
s1.discard(30)
print(s1)
'''
#pop()
'''
s1 = {1,2,3,4,5}
print(s1)
s1.pop()
print(s1)
'''
#clear()
'''
s1 = {1,2,3,4,5}
print(s1)
s1.clear()
print(s1)
'''
#Del Keyword
'''
s1 = {1,2,3,4}
print(s1)
del s1
print(s1)
'''
#Built in function
'''
s1 = {1,3,2,4}
#sum()
print(sum(s1))
#max()
print(max(s1))
#min()
print(min(s1))
#all()
print(all(s1))
#any()
print(any(s1))
#sorted()
print(sorted(s1))
'''

#Frozen sets
#Creation
'''
#Homogeneous
s1 = frozenset()
print(s1)
print(type(s1))
s2  = frozenset([1,2,3,4])
print(s2)
print(type(s2))
#Hetrogeneous X
'''
#Accessing
#union()
#copy()
#intersection()
#difference()
#symmetric_difference()
#isdisjoint()
#issuperset()
#issubset()


