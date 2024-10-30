#University Management System
class person:
    def __init__(self,name,roll,mobile):
        self.name = name
        self.roll = roll
        self.mobile = mobile
class student(person):
    def __init__(self,name,roll,mobile,branch):
        self.branch = branch
        super().__init__(name,roll,mobile)
class teacher(person):
    def __init__(self,name,roll,mobile,subject):
        self.subject = subject
        super().__init__(name,roll,mobile)
class college:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.teachers = []
    def add_student(self,student):
        self.students.append(student)
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    def display_students(self):
        print()
        for i in range(len(self.students)):
            print(f"Student {i+1} Details")
            print(f"Name: {self.students[i].name}")
            print(f"Roll Number: {self.students[i].roll}")
            print(f"Mobile Number: {self.students[i].mobile}")
            print(f"Branch: {self.students[i].branch}")
            print()
    def display_teachers(self):
        print()
        for i in range(len(self.teachers)):
            print(f"Teacher {i+1} Details")
            print(f"Name: {self.teachers[i].name}")
            print(f"Roll Number: {self.teachers[i].roll}")
            print(f"Mobile Number: {self.teachers[i].mobile}")
            print(f"Subject: {self.teachers[i].subject}")
            print()
colleges = []
while True:
    print("Choose your Option")
    print("1. For Create College")
    print("2. To add student")
    print("3. to add Teacher")
    print("4. Display students Details")
    print("5. Display Teachers Details")
    print("6. Exit")
    x = int(input("Enter your Option: "))
    if x == 1:
        cname = input("Enter College Name: ")
        x = True
        for i in colleges:
            if i.name == cname:
                x = False
                break
        if x == True:
            c = college(cname)
            colleges.append(c)
            print("College Created Sucessfully")
        else:
            print("College already Exists")
    elif x == 2:
        cname = input("Enter College Name: ")
        x = False
        for i in colleges:
            if i.name == cname:
                x = True
        if x == True:
            ind = -1
            for i in range(len(colleges)):
                if colleges[i].name == cname:
                    ind = i
            sname = input("Enter Student name: ")
            sroll = input("Enter Roll number: ")
            smobile = input("Enter Mobile Number: ")
            sbranch = input("Enter student Branch: ")
            s1 = student(sname,sroll,smobile,sbranch)
            colleges[ind].add_student(s1)
            print(f"Student added to {cname} college")
        else:
            print("College not exists")
    elif x == 3:
        cname = input("Enter College Name: ")
        x = False
        for i in colleges:
            if i.name == cname:
                x = True
        if x == True:
            ind = -1
            for i in range(len(colleges)):
                if colleges[i].name == cname:
                    ind = i
            tname = input("Enter Teacher name: ")
            troll = input("Enter Roll number: ")
            tmobile = input("Enter Mobile Number: ")
            tsubject = input("Enter Subject: ")
            t1 = teacher(tname,troll,tmobile,tsubject)
            colleges[ind].add_teacher(t1)
            print(f"Teacher added to {cname} college")
        else:
            print("College not exists")
    elif x == 4:
        cname = input("Enter college name: ")
        x = False
        for i in colleges:
            if i.name == cname:
                x = True
        if x == True:
            ind = -1
            for i in range(len(colleges)):
                if colleges[i].name == cname:
                    ind = i
            colleges[ind].display_students()
        else:
            print("College not exists")
    elif x == 5:
        cname = input("Enter college name: ")
        x = False
        for i in colleges:
            if i.name == cname:
                x = True
        if x == True:
            ind = -1
            for i in range(len(colleges)):
                if colleges[i].name == cname:
                    ind = i
            colleges[ind].display_teachers()
        else:
            print("College not exists")
    else:
        break
            
'''
c1 = college("kits")
s1 = student("sai",101,9123456789,"CSE")
s2 = student("vardhan",102,789654321,"ECE")
c1.add_student(s1)
c1.add_student(s2)
c1.display_students()
t1 = teacher("sai vardhan",201,9876543211,"Python")
t2 = teacher("malli",202,9876543211,"Java")
c1.add_teacher(t1)
c1.add_teacher(t2)
c1.display_teachers()
'''




