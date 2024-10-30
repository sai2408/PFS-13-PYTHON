#Problem - 3
#Approach - 1
'''
class sample:
    def __init__(self):
        print("Hello")
class child(sample):
    def __init__(self):
        super().__init__()
ch = child()
'''
#approach - 2
'''
class sample:
    def hello(self):
        print("hello")
class child(sample):
    def hello(self):
        super().hello()
ch = child()
ch.hello()
'''
#Problem - 4
'''
class sample:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        x = self.a + self.b
        return x
    def subtraction(self):
        x = self.a - self.b
        return x
    def multiplication(self):
        x = self.a * self.b
        return x
obj = sample(10,5)
print(obj.addition())
print(obj.subtraction())
print(obj.multiplication())
'''
#Problem - 5
'''
class abc:
    def __init__(self,a):
        self.a = a
    def factorial(self):
        res = 1
        for i in range(2,self.a+1):
            res = res * i
        print(res)
    def prime_number(self):
        x = True
        for i in range(2,self.a):
            if self.a%i == 0:
                x = Falsse
                break
        if x == True:
            print("Prime number")
        else:
            print("Not a prime number")
obj = abc(15)
obj.factorial()
obj.prime_number()
'''
#Problem - 6
#Approach - 1
'''
class dob:
    def __init__(self,date,month,year):
        self.date = date
        self.month = month
        self.year = year
    def display(self):
        return f"{self.date}-{self.month}-{self.year}"
class details(dob):
    def __init__(self,name,date,month,year):
        self.name = name
        super().__init__(date,month,year)
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.display()}")
d = details("sai",24,8,2024)
d.display_details()
'''
#Approach - 2
'''
class dob:
    def __init__(self,date,month,year):
        self.date = date
        self.month = month
        self.year = year
    def display(self):
        print(f"Date of birth: {self.date}-{self.month}-{self.year}")
class details(dob):
    def __init__(self,name,date,month,year):
        self.name = name
        super().__init__(date,month,year)
    def display_details(self):
        print(f"Name: {self.name}")
        self.display()
d = details("sai",24,8,2024)
d.display_details()
'''
#Problem - 7
#Approach - 1
'''
class college:
    cname = "SV"
    location = "TPT"
class cse(college):
    def __init__(self,sid,sname):
        self.sname = sname
        self.sid = sid
    def display(self):
        print(f"Name: {self.sname}")
        print(f"Roll: {self.sid}")
        print(f"College name: {self.cname}")
        print(f"College Location: {self.location}")
class aiml(college):
    def __init__(self,sid,sname):
        self.sname = sname
        self.sid = sid
    def display(self):
        print(f"Name: {self.sname}")
        print(f"Roll: {self.sid}")
        print(f"College name: {self.cname}")
        print(f"College Location: {self.location}")     
s1 = cse("sai",101)
s1.display()
s2 = aiml("vardhan",201)
s2.display()
'''
#Appraoch - 2
'''
class college:
    def __init__(self,cname="sv",location="tpt"):
        self.cname = cname
        self.location = location
class cse(college):
    def __init__(self,sid,sname):
        self.sname = sname
        self.sid = sid
        super().__init__()
    def display(self):
        print(f"Name: {self.sname}")
        print(f"Roll: {self.sid}")
        print(f"College name: {self.cname}")
        print(f"College Location: {self.location}")
class aiml(college):
    def __init__(self,sid,sname):
        self.sname = sname
        self.sid = sid
        super().__init__()
    def display(self):
        print(f"Name: {self.sname}")
        print(f"Roll: {self.sid}")
        print(f"College name: {self.cname}")
        print(f"College Location: {self.location}")     
s1 = cse("sai",101)
s1.display()
s2 = aiml("vardhan",201)
s2.display()
'''
#Problem - 9
'''
#Approach - 1

class vehicle:
    def __init__(self,model):
        self.model = model
    def display3(self):
        print(f"Model: {self.model}")
class motor(vehicle):
    def __init__(self,mtype,model):
        self.mtype = mtype
        super().__init__(model)
    def display2(self):
        print(f"Motor type: {self.mtype}")
class car(motor):
    def __init__(self,name,mtype,model):
        self.name = name
        super().__init__(mtype,model)
    def display1(self):
        print(f"Name: {self.name}")
c1 = car("thar","Mahindra",2024)
c1.display1()
c1.display2()
c1.display3()
'''
#Approach - 2
'''
class car:
    def __init__(self,name,mtype,model):
        self.name = name
        self.mtype = mtype
        self.model = model
    def display1(self):
        print(f"Name: {self.name}")
class motor(car):
    def display2(self):
        print(f"Motor Type: {self.mtype}")
class vehicle(car):
    def display3(self):
        print(f"Model: {self.model}")    
c1 = car("thar","Mahindra",2024)
c1.display1()
c1.display2()
c1.display3()   
'''













































