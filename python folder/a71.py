#71 lecture 
# __dict__ attribute,help()
# class Person:
#     def __init__(self,name,age,version):
#         self.name=name
#         self.age=age
#         self.version=version
# p=Person("John",20,3)
# print(p.__dict__)

# print(help(Person))

#72 lecture
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
rohan=Employee("Rohan","421")
Abhi=Programmer("Abhi","2345","Python")

print(Abhi.name)
print(Abhi.id)
print(Abhi.lang)
# print(rohan.name)

#73 lecture

#74 lecture
#Method overloading
class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def area(self):
        return self.x*self.y
    
class Circle(Shape):    #inheritance
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)     #super keyword
    
    def area(self):
        return 3.14*super().area()  #Method overloading
    
c=Circle(5)
print(c.area())
    
    
#78 lecture 
#Operator Overloading
class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    
    def __str__(self):
        return f'{self.i}i+{self.j}j+{self.k}k'
    
    def __add__(self,x):        #operator Overloading
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
v1=Vector(3,5,6)
print(v1)
v2=Vector(3,5,6)
print(v2)
print(v1+v2)
print(type(v1+v2))

#79 lecture
#Single Inheritance 
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def make_sound(self):
        print("Sound made by the Animal")
        
class Dog(Animal):      #Inheritance
    
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed
    
    def make_sound(self):
        print("Bark!")
        
d=Dog("Dog","Doggerman")
d.make_sound()

a=Animal("Dog","Dog")
a.make_sound()

#80 lecture
#Multiple Inheritance
class Employees:
    def __init__(self,name):
        self.name=name
    
    def show(self):
        print(f"The name is {self.name}")
        
class Dancer:
    def __init__(self,dance):
        self.dance=dance
        
    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employees,Dancer):       #Multipe Inheritance
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name
        
o=DancerEmployee("Kathak","Ab")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())
