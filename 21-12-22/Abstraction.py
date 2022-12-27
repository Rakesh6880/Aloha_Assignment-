


# Abstraction
from abc import ABC,abstractmethod
class Parent(ABC):
    def __init__(self,a):
        self.a=a
    @abstractmethod
    def method_1(self):
        pass
    @abstractmethod
    def method_2(self):
        pass
class Child(Parent):
    def __init__(self,a):
        Parent.__init__(self,a)
    def method_1(self):
        print("method",self.a)
class Child1(Child):
    def __init__(self,a):
        Child.__init__(self,a)
    def method_2(self):
        print("Method 2",self.a)
ob=Child1(3)
ob.method_2()
