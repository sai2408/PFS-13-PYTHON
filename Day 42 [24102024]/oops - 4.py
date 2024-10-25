#single Inheritance
#Problem - 1
'''
class Parent:
    def hello(self):
        print("Hello from Parent class")
class child(Parent):
    def bye(self):
        print("Bye from child class")
c1 = child()
c1.hello()
c1.bye()
c2 = Parent()
c2.hello()
c2.bye()
'''
#Problem - 2
'''
class Parent:
    def __init__(self):
        print("Constructor of Parent Class")
class child(Parent):
    def __init__(self):
        print("constructor of Child class")
c1 = child()
c2 = Parent()
'''
#Problem - 3
'''
class Parent:
    def hello(self):
        print("Hello from Parent Class")
class child(Parent):
    def __init__(self):
        print("constructor of Child class")
c1 = child()
c1.hello()
'''
#Problem - 4
'''
class Parent:
    def __init__(self):
        print("constructor of Parent class")
class child(Parent):
    def hello(self):
        print("Hello from Parent Class")
c1 = child()
c1.hello()
'''
#Multiple Inheirtance
#Problem - 1
'''
class Parent1:
    def hello1(self):
        print("Hello from Parent 1")
class Parent2:
    def hello2(self):
        print("Hello from Parent 2")
class child(Parent1,Parent2):
    def hello3(self):
        print("Hello from Parent 3")
c1 = child()
c1.hello1()
c1.hello2()
c1.hello3()
c2 = Parent2()
c2.hello2()
c1 = Parent1()
c1.hello1()
'''
#Problem - 2
'''
class Parent1:
    def hello(self):
        print("Hello from Parent 1")
class Parent2:
    def hello(self):
        print("Hello from Parent 2")
class child(Parent2,Parent1):
    def hello1(self):
        print("Hello from Parent 3")
c1 = child()
c1.hello()
'''
#Problem - 3
'''
class parent1:
    def __init__(self):
        print("parent 1")
class parent2:
    def __init__(self):
        print("parent 2")
class child(parent1,parent2):
    def __init__(self):
        print("child")
    def hello(self):
        print("hello")
c1 = child()
'''
#Problem - 4
'''
class parent1:
    def __init__(self):
        print("parent 1")
class parent2:
    def __init__(self):
        print("parent 2")
class child(parent1,parent2):
    def hello(self):
        print("hello")
c1 = child()
'''
#Problem - 5
'''
class parent1:
    def __init__(self):
        print("parent 1")
class parent2:
    def __init__(self):
        print("parent 2")
class child(parent2,parent1):
    def hello(self):
        print("hello")
c1 = child()
'''
#Problem - 6
'''
class parent1:
    def hello1(self):
        print("hello 1")
class parent2:
    def __init__(self):
        print("parent 2")
class child(parent1,parent2):
    def hello(self):
        print("hello")
c1 = child()
'''
#Multi Level Inheiritance
#Problem - 1
'''
class parent:
    def hello1(self):
        print("Hello from Parent")
class child1(parent):
    def hello2(self):
        print("Hello from child 1")
class child2(child1):
    def hello3(self):
        print("Hello from child 3")
c1 = child2()
c1.hello1()
c1.hello2()
c1.hello3()
c2 = child1()
c2.hello1()
c2.hello2()
c3 = parent()
c3.hello1()
'''
#Hirarichal Inheritance
#Problem - 1
'''
class parent:
    def hello(self):
        print("Hello From parent class")
class child1(parent):
    def hello1(self):
        print("Hello from child class 1")
class child2(parent):
    def hello2(self):
        print("Hello from child class 2")
c1 = child2()
c1.hello2()
c1.hello()
c2 = child1()
c2.hello1()
c2.hello()
c3 = parent()
c3.hello()
'''
#Super Method
'''
class parent:
    def abc(self):
        print("hello from parent")
class child(parent):
    def abc(self):
        super().abc()
        #print("hello from child")
c = child()
c.abc()
'''
#Super method
'''
class parent:
    def abc(self):
        print("hello from parent")
class child(parent):
    def abc(self):
        print("Hello from child")
        super().abc()
c = child()
c.abc()
'''


















































        
