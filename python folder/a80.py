class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
        
    def show_details(self):
        print(f"Name:{self.name}")
        print(f"Species:{self.species}")
        
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed
    
    def show_details(self):
        Animal.show_details(self)
        print(f'Breed: {self.breed}')
        
class GoldenRetriever(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="Golden Retriever")
        self.color=color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color:{self.color}")
        
o=GoldenRetriever("Tommy","Skin")
o.show_details()
print(GoldenRetriever.mro())

#81 lecture
#Hybrid Inheritance
# class Baseclass:
#     pass
# class Derived1(Baseclass):
#     pass
# class Derived2(Baseclass):
#     pass
# class Derived3(Derived1,Derived2):
#     pass

class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
    
class Person(Human):
    def __int__(self,name,age,address):
        Human.__init(self,name,age)
        self.address=address
    
    def show_details(self):
        Human.show_details(self)
        print("Address:",self.address)
        
class Program:
    def __init__(self,program_name,duration):
        self.program_name=program_name
        self.duration=duration
    
    def show_details(self):
        print("Program Name:",self.program_name)
        print("Duration:",self.duration)
        
class Student(Person):
    def __init__(self,name,age,address,program):
        Person.__init__(self,name,age,address)
        self.program=program

    def show_details(self):
        Person.show_details(self)
        self.program.show_details()

