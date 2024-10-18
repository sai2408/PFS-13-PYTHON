#Problem - 1
'''
import re
pattern1 = re.compile(r'\d{2}-\d{2}/\d{4}')
pattern2 = re.compile(r'\d{3}-\d{3}-\d{4}')
text1 = input("Enter Date of birth in dd-mm/yyyy format: ")
text2 = input("Enter Mobile Number in xxx-xxx-xxxx format: ")
matches1 = re.findall(pattern1,text1)
if len(matches1) == 0:
    print("Give DOB in correct format")
else:
    print(matches1[0])
matches2 = re.findall(pattern2,text2)
if len(matches2) == 0:
    print("Give Mobile number in correct format")
else:
    print(matches2[0])
'''
#Problem - 2
'''
import re
pattern = re.compile(r'.+@gmail.com')
text = input("Enter gmail id: ")
matches = re.findall(pattern,text)
if len(matches) == 0:
    print("Give Gmail id in correct format")
else:
    print(matches[0])
'''
#Problem - 3
'''
import re
pattern = re.compile(r'[a-zA-Z0-9]+')
text = input("Enter your username:  ")
matches = re.findall(pattern,text)
if len(matches) == 0:
    print("Give username in correct format")
else:
    print(matches[0])
'''



























