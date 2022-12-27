class Values:
   def __init__(self):
      self.a = 123
      self._b = 123
      self.__c = 123

obj = Values()
print(obj.a)
print(obj._b)
#print(obj.__c) # Error

class Value:
   def __init__(self):
      self.__value = 200

   def getValue(self):
      print(self.__value)

   def setValue(self, value):
      self.__value = value

obj = Value()
obj.getValue()
obj.setValue(20)
obj.getValue()
print(obj.__value)

