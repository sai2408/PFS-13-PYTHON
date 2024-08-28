#Strings
#Creation
#Homogenious elements
'''
s = "python"
print(s)
print(type(s))
'''
#Hetrogeneous elements
#Accessing
#Indexing
'''
s = "Sai Vardhan"
#Positive Indexing
print(s[0])
print(s[4])
#Negetive Indexing
print(s[-1])
print(s[-6])
'''
#Looping
#Slicing
'''
s = "saivardhan"
print(s)
print(s[::])
print(s[:])
print(s[::1])
print(s[0:3])
print(s[:3])
print(s[3:10])
print(s[3::1])
print(s[3:])
print(s[2:7])
print(s[::2])
print(s[1::2])
print(len(s[1::2]))
print(s[::-1])
'''
#Methods
'''
s = "saivardhan"
print(s.endswith("sa"))
print(s.endswith("an"))
print(s.endswith("saivardhan"))
print(s.startswith("vardhan"))
print(s.startswith("s"))
print(s.startswith("sai"))
s1 = "100"
print(s1.isdigit())
print(s1.isdecimal())
s2 = "abc"
print(s1.isalpha())
print(s2.isalpha())
s3 = "abc123"
print(s3.isalpha())
print(s3.isdigit())
print(s3.isalnum())
print(s1.isalnum())
print(s2.isalnum())
s4 = "sai vardhan"
print(s4.istitle())
s5 = "sai"
print(s5.upper())
print(s5)
s7 = "SAI"
print(s7.lower())
s8 = "Sai Vardhan"
print(s8.swapcase())
s9 = "sai vardhan"
print(s9.capitalize())
print(s9.find("a"))
print(s9.rfind("a"))
print(s9.count("a"))
'''
#Insertion
'''
s1 = "sai"
s1 = s1 + "Vardhan"
print(s1)
'''
#Deletion
'''
s1 = "sai"
print(s1)
del s1
print(s)
'''
#Updation
'''
s1 = "Sai Vardhan"
print(s1.replace("a","x"))
print(s1)
s1 = s1.replace("a","x")
print(s1)
'''













