# Inheritance
class Parent:
    def __init__(self,fname,fage):
        self.name=fname
        self.age=fage
    def func(self):
        print(self.name,self.age)
class Child(Parent):
    def __init__(self,fname,fage,fusn):
        Parent.__init__(self,fname,fage)
        self.usn=fusn
    def func1(self):
        print(self.usn,self.name,self.age)
ob1=Child("Rakhi",20,69)
ob1.func()
ob1.func1()


# Multiple Inheritance
class Parent:
    def func1(self):
        print("This is func 1")
class Parent1:
    def func2(self):
        print("This is func 2")
class Child(Parent,Parent1):
    def func3(self):
        print("This is func 3")
ob=Child()
ob.func2()
ob.func1()
ob.func3()


# Multiple Inheritance

class Parent:
    def func1(self):
       print("This is a Parent")
class Child(Parent):
    def func2(self):
        print("This is a Child")
class Subchild(Child):
    def func3(self):
        print("This is a Sub Child")
ob=Subchild()
ob.func1()
ob.func2()
ob.func3()


# Super Function
class Parent:
    def func1(self):
        print("This is a Function 1")
class Child(Parent):
    def func2(self):
        print("This is Function 2")
        super().func1()
ob=Child()
ob.func2()