# #f-string
name ="Abhi"
country ="India"
print(f"Hey my name is {name} and I am from {country}")

price = 29.9533
print(f"For only {price:.2f} Rupees")

#Lecture 29 DocString
def square(n):
    '''Takes a number n, returns the square of a number n'''
    print(n**2)
square(5)
print(square.__doc__)

#Lecture 30
#Recursion in python
#Factorial example
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#Fibonacci Sequence
def fibonacci(n):
    if (n<0):
        print("Invalid")
    elif(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(9))

#Lecture 31
#sets 
#set is an collection of unordered data items
s={1,2,3,4,5,1}
print(s)
info={"Abhi",1,1,5.9,False,"Hello"}
print(info)
inf={True}
print(inf)

#lecture32
#set methods
#union() and update() function
s1={1,2,3,45,1}
s2={3,4,5,6}
print(s1.union(s2))
print(s1,s2)
s1.update(s2)
print(s1,s2)

#2.intersection() and intersection_update()
cities={"Delhi","Tokyo","Goa","Bangalore"}
cities2={"Goa","Bangalore","Mumbai","Delhi"}
cities.intersection_update(cities2)
print(cities)

#3.Symmetric_difference() andd symmetric_difference_update()
cities={"Delhi","Tokyo","Goa","Bangalore"}
cities2={"Goa","Bangalore","Mumbai","Delhi"}
cities3=cities.symmetric_difference(cities2)
print(cities3)

#4.difference() and difference_update()
cities={"Delhi","Tokyo","Goa","Bangalore"}
cities2={"Goa","Bangalore","Mumbai","Delhi"}
cities4=cities.difference(cities2)
print(cities4)

#isdisjoint()
cities={"Delhi","Tokyo","Goa","Bangalore"}
cities2={"Goa","Bangalore","Mumbai","Delhi"}
cities5=cities.isdisjoint(cities2)
print(cities5)

#5.issuperset()
cities={"Delhi","Tokyo","Goa","Bangalore"}
cities2={"Goa","Bangalore","Mumbai","Delhi"}
cities5=cities.issuperset(cities2)
print(cities5)

#6.issubset() basically it is a reverse of superset()
city={"Tokyo","Madrid","Berlin","Delhi"}
city2={"Seoul","Dubai"}
city3={"Tokyo","Madrid","Delhi"}
print(city3.issubset(city))


#7.add()function
cityn1 ={"Madrid","Goa","Mumbai"}
cityn1.add("Delhi")
print(cityn1)

#8.update()
cityn2 ={"Madrid","Goa","Mumbai"}
cityn3={"Tokyo","Madrid","Delhi"}
cityn2.update(cityn3)
print(cityn2)

#remove()/discard()

#pop()
citynames={"Berlin","Tokyo","Delhi"}
item =citynames.pop()
print(citynames)
print(item)

#clear()
citya={"Tokyo","Goa"}
citya.clear()
print(citya)

#del()
cityy={"Tojyo","Goa"}
del cityy
print(cityy)
