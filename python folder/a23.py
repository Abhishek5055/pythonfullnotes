#List methods
l=[2,3,4,88,99,54,100,89,98,99,99,100]
print(l)    #it will display the list items
l.sort()    #print in ascending order
print(l)
l.sort(reverse=True)    #print in descending order
print(l)
l.append(99)        #it will add element to the list
print(l)
l.reverse()     #it will reverse the original list
print(l)

list2=[1,2,3,4,5,6,7,8,1]
print(list2.index(1))       #it will returns the index of the dirst occurence of the list
print(list2.count(1))       #count the number of items in the given value

#copy()
list3=[1,2,3,5,5,6]
m=list3.copy()
m[0] = 0
print(list3)
list3.insert(1,900) #inser() function usage
print(list3)
m=[900,800,999]
list3.extend(m) #extend()function usage
print(list3)

c=["Ab","bc","cd"]
c2=["De","Fg","Gh"]
print(c+c2)

#24th lecture
#Tuples are unchangegable unlike lists,Tuples are immutable
tup = (1,2,56,77,99)
print(tup)

#25 th Lecture
#Manipulating tuple Example1

countries =("Spain","Italy","India","Usa")
temp =list(countries)
temp.append("Russia")
temp.pop(3)
temp[1] ="Finland"
countries =tuple(temp)
print(countries)

#Example 2
tuple2=(1,2,3,4,3,5,6,3,8)
res = tuple2.index(3)
print("The index of 3 is:",res)

#26th lecture
#Excercise 2 greeting good morning according to Time
import time
t = time.strftime("%H:%M:%S")
print(t)
h = int(time.strftime("%H"))

if(h>=0 and h<12):
    print("Good Morning")
elif(h>=12 and h<17):
    print("Good Evening")
else:
    print("Good Night")
    
#27 is the excercise 3 problem like kbc we should ask question.