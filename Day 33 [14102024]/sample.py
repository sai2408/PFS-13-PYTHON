#Read
'''
f1 = open("hello1.txt","r")
print(f1.read())
f1.close()
'''
#Write
#Case 1
'''
f2 = open("hello2.txt","w")
f2.write("This is hello 2 file")
f2.close()
'''
#Case 2
'''
f3 = open("hello3.txt","w")
f3.write("Hello everyone")
f3.close()
'''
#Append
'''
f4 = open("hello4.txt","a")
f4.write(" Codegnan")
f4.close()
'''
#Read and Write
'''
f5 = open("hello5.txt","r+")
print(f5.read())
f5.seek(6)
f5.write("Codegnan")
f5.seek(0)
print(f5.read())
f5.close()
'''
#Problem - 1
'''
f6 = open("hello6.txt","r+")
print(f6.read())
f6.write("\nWelcome to Codegnan")
f6.close()
'''
#Problem - 2
'''
f = open("Details.txt","r+")
f.seek(17)
f.write("\n")
n = int(input("enter no of employees: "))
for i in range(n):
    name = input("enter employee name: ")
    sal = input("Enter Employee salary: ")
    sub = input("enter employee subject: ")
    f.write(f"\nEmployee name: {name}")
    f.write(f"\nEmployee Salary: {sal}")
    f.write(f"\nEmployee Subject : {sub}")
    f.write("\n")
f.close()
'''
    




















