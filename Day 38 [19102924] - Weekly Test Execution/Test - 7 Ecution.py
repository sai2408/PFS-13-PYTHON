#Problem - 1
#Appraoch - 1
'''
f = open("hello.txt","r")
print(f.read())
f.close()
'''
#Appraoch - 2
'''
f = open("hello.txt","r")
x = f.read()
print(x)
f.close()
'''
#Problem - 2
#Approach - 1
'''
f = open("test.txt","w")
f.write("Hello world\nHello Codegnan")
f.close()
'''
#Approach - 2
'''
f = open("test.txt","w")
f.write("Hello world\n")
f.write("Hello Codegnan")
f.close()
'''
#Problem - 3
#Approach - 1
'''
from os import *
mkdir("abc")
chdir("xyz")
print(listdir())
'''
#Approach - 2
'''
from os import *
mkdir("abc")
chdir("xyz")
x = listdir()
print(x)
'''
#Problem - 4
#Approach -1 
'''
import re
pattern = r'\s'
text = "My name is codegnan"
matches = re.findall(pattern,text)
print(len(matches))
'''
#Approach -2
'''
import re
pattern = re.compile(r'\s')
text = "My name is codegnan"
matches = re.findall(pattern,text)
print(len(matches))
'''
#Problem - 5
#Appraoch - 1
'''
import re
pattern = r'\W'
text = "Hello Codegnan $"
matches = re.findall(pattern,text)
print(matches)
'''
#Approach - 2
'''
import re
pattern = re.compile(r'\W')
text = "Hello Codegnan $"
matches = re.findall(pattern,text)
print(matches)
'''
#Problem - 6
#Approach - 1
'''
import re
pattern = r'\bhello\b'
text = "Hello World hello"
matches = re.findall(pattern,text)
print(len(matches))
'''
#Appraoch - 2
'''
import re
pattern = re.compile(r'\bhello\b')
text = "Hello World hello"
matches = re.findall(pattern,text)
print(len(matches))
'''
#Problem - 7
#Approach - 1
'''
import re
pattern = r'^hello'
text = "world hello"
matches = re.findall(pattern,text)
print(matches)
'''
#Approach - 2
'''
import re
pattern = r'^hello'
text = "hello world hello"
matches = re.findall(pattern,text)
if len(matches) == 0:
    print("Not starting with hello")
else:
    print("starting with hello")
'''
#Problem - 8
'''
import re
pattern = r'ab{3}'
text = "abbb"
matches = re.search(pattern,text)
print(matches)
'''
#Problem - 9
'''
import re
pattern = r'\d{7}-\d{4}'
text = input()
matches = re.findall(pattern,text)
print(matches)
'''
#Problem - 10
'''
import re
p1 = r'.+@gmail.com'
p2 = r'\d{2}-\d{2}/\d{4}'
t1 = input()
t2 = input()
m1 = re.findall(p1,t1)
print(m1)
m2 = re.findall(p2,t2)
print(m2)
'''

































