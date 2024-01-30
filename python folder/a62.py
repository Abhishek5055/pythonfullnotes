#62
#Access Modifiers
#Examople 1 Public
class Employee:
    def __init__(self):
        self.name="Abhi1"
a=Employee()
print(a.name)

#Example 2
#private access modifiers
class Employee:
    def __init__(self):
        self.__name="Abhi2"
a=Employee()
#print(a.__name)#you cannot access like this directly
print(a._Employee__name)        #you can access indirectly

#Example 3
#Protected Access Modidier
class Student:
    def __init__(self):
        self._name="Abhi"
    def _funName(self): #protected method
        return "Abhishek"
class Subject(Student):     #inherited class
    pass
obj=Student()
obj1=Subject()

#Calling by object of Student Class
print(obj._name)
print(obj._funName())

#Calling by object of Subject Class
print(obj1._name)
print(obj1._funName())