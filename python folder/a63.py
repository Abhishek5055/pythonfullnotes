# # #63 lecture
# # #Exercise 5
# # #Snake Water Gun
# # import random
# # def check(comp,user):
# #     if(comp==user):
# #         return 0
# #     if(comp==0 and user==1):
# #         return -1
# #     if(comp==1 and user==2):
# #         return -1
# #     if(comp==2 and user==0):
# #         return -1
# #     return 1
# # comp = random.randint(0,2)
# # user=int(input("0 for Snake,1 for Water,2 for Gun:\n"))

# # score=check(comp,user)
 
# # print("You:",user)
# # print("Computer:",comp)

# # if(score==0):
# #     print("It is a draw")
# # elif(score==-1):
# #     print("You Lose")
# # else:
# #     print("You Won")


# # #64 lecture
# # #Library Mangement System



# # #65 lecture
# # class Emp:
# #     @staticmethod       #static
# #     def add(a,b):
# #         return a+b
# # result=Emp.add(1,2)
# # print(result)

# # #Example 2
# # class Emps:
# #     def __init__(self,num):
# #         self.num=num
# #     def addtonum(self,n):
# #         self.num=self.num+n
# #     @staticmethod
# #     def add(a,b):
# #         return a+b
    
# # a = Emps(5)
# # print(a.num)
# # a.addtonum(6)
# # print(a.num)
# # print(Emps.add(2,3))
    
# #66 lecture
# #Class Variable
# class MyClass:
#     class_variable=0
    
#     def __init__(self):
#         MyClass.class_variable+=2
#     def print_class_variable(self):
#         print(MyClass.class_variable)
# obj1=MyClass()
# obj2=MyClass()

# obj1.print_class_variable()
# obj2.print_class_variable()

# #Instance Variable
# #Example
# class MyClass2:
#     def __init__(self,name):
#         self.name=name
#     def print_name(self):
#         print(self.name)
# obj1=MyClass2("Abhi")
# obj2=MyClass2("Ro")

# obj1.print_name()
# obj2.print_name()

#67 lecture
# class Library:
#     def __init__(self):
#         self.noBooks =0
#         self.books = []
#     def addBook(self,book):
#         self.books.append(book)
#         self.noBooks = len(self.books)
#     def showInfo(self):
#         print(f"The library has {self.noBooks} books.The books are")
#         for book in self.books:
#             print(book)
# l1=Library()
# l1.addBook("Harry Potter1")
# l1.addBook("Harry Potter2")
# l1.addBook("Harry Potter3")
# l1.showInfo()
        
# #69 lecture
# class Emp:
#     company="Apple"
#     def show(self):
#         print(f"The name is {self.name} and company is {self.company}")
        
#     @classmethod
#     def changeCompany(cls,newcompany):
#         cls.company=newcompany
# e1=Emp()
# e1.name="Abhi"
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# print(Emp.company)

#70 lecture
#class methood as an alternative constructor
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_string(cls,string):
        name,age=string.split(',')
        return cls(name,int(age))
    
person = Person.from_string("John ,30")
print(person.name,person.age)      