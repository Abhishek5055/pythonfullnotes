# #59 lecture
# #decorators
# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx

# @greet
# def hello():
#     print("Hello World")
# hello()

# #Example 2 
# #with arguments are present the do like this
# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("Good Morning")
#         fx(*args,**kwargs)
#         print("Thanks for using this function")
#     return mfx

# @greet
# def hello():
#     print("Hello World")
# hello()
# @greet
# def add(a,b):
#     print(a+b)
# add(1,2)
    
    
#60 Lecture
#Getters and Setters
class MyClass:
    def __init__(self,value):
        self._value =value
        
    def show(self):
        print(f"Value is{self._value}")
        
    @property       #getter
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter       #setter
    def ten_value(self,new_value):
        self._value =new_value/10
        
    
obj = MyClass(10)
obj.ten_value =67
print(obj.ten_value)
obj.show()

#61 lecture
#Inheritance
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The name of the employee {self.id} is {self.name}")
        
class Programmer(Employee):
    def showLanguage(self):
        print("The Default Language is Python")
        
e1=Employee("Rohan",400)
e1.showDetails()
e2=Programmer("Abhi",99)
e2.showDetails()
e2.showLanguage()