#Function arguments and return statement
#i)deault arguments

def average(a=10,b=4):
    print("The Average is ",(a+b)/2)
    
average()

#Keyword Arguments
def aveage(a,b):
    print("The Averge is:",(a+b)/2)
average(b=4,a=10)      #in keyword argument we have the power to change the argument.

#Required Argument
def average(a, b, c=10):
    print("The Average is",(a+b+c)/3)
average(10,4)

#KEyword Argument
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("The Average is:",sum/len(numbers))
average(5,6,7)

#return statement
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum / len(numbers)
c=average(4,4,4,4,)
print(c)

#day 22 of python
#lists
l=[3,4,5,6]
print(l)
marks=[2,3,"Abhi",4,True]
print(marks)
print(l[-2])

#To print all the elements in  the list
print(marks)
print(marks[:])
print(marks[1:])  #it will stasrt from the first index
#negative indexing
print(marks[1:-1])
print(marks[1:4])

#Jump index usage
score=[35,100,100,99,96,99,97,100,100,100,60,60,99,99,99,99,99,100,100,100]
print(score[1:20])
print(score[1:20:2]) #jump index usage

#List comprehension
lst=[i*i for i in range(4)]
print(lst)
#list comprehension with condition
lst2=[i*i for i in range(10) if(i%2==0)]
print(lst2)
                                                                                                                                       