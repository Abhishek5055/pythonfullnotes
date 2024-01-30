#54 lecture
a=3
b=3
print(a is b)
print(a==b)
c=[23,34,45]
d=[23,34,45]
print(c is d)
print(c==d)


#55 lecture
#Exercise 5

#56 Lecture #just introduction to OOPS Concept

#57 lecture #Class and Objects
class Person:
    name='Abhi'
    occupation='Software developer'
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a = Person()
a.info()

class Pers:
    name='Abhi'
    occupation='Software developer'
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a=Pers()
b=Pers()

a.name='Abhishek'
a.occupation="Software Developer"

b.name="Me"
b.occupation="CEO"

a.info()
b.info()

#58 Lecture
class Persons:
    def __init__(self):
        print("Hey I am a person")
    def info(self):
        print(f"{self.name} is a {self.occupation}")
e=Persons()
f=Persons()


#Example 1
#parameterized Constructor
class Details:
    def __init__(self,animal,group):
        self.animal=animal
        self.group=group
obj1=Details("Crab","Crustaceans")
print(obj1.animal,"Belongs to the",obj1.group,"group")

#Example 2
#Default Constructor
class Details2:
    def __init__(self):
        print('crab Belongs to the group Crustaceans.')
obj1=Details2()

