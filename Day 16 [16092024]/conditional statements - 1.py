#Conditional Statements
#If
'''
age = int(input("Enter your Age: "))
vc = input("Do you have Voter card (y/n) : ")
if ((age>=18) and (vc=="y")):
    print("Yes, you can Vote")
print("Outside If block")
'''
#If - Else
'''
age = int(input("Enter your Age: "))
vc = input("Do you have Voter card (y/n) : ")
if ((age>=18) and (vc=="y")):
    print("Yes, You can vote")
else:
    print("No, You can't Vote")
print("Outside ifelse block")
'''
#Elif
'''
age = int(input("Enter your Age: "))
vc = input("Do you have Voter card (y/n) : ")
if ((age>=18) and (vc=="y")):
    print("Yes, You can vote")
elif ((age<=17) and (vc=="y")):
    print("Can vote, but does not have eligibility")
else:
    print("No, You can not vote")
print("Outside if-elif-else block")
'''
#Nested Conditional statements
'''
age = int(input("Enter your Age: "))
vc = input("Do you have Voter card (y/n) : ")
if (age>=18):
    if (vc=="y"):
        print("Yes, You can vote")
    else:
        print("Eligible, But need voter card")
else:
    if (vc=="y"):
        print("Can vote, But illegal")
    else:
        print("No, you can not vote")
'''
#Conditional Expression
'''
age = int(input("Enter Your Age: "))
res = "Can vote" if age>=18 else "Can not Vote"
print(res)
'''












