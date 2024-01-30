#84 lecture
#Time Module in Python
import time
print(time.time())

print(4)
time.sleep(4)
print("This is printed after 4 seconds of sleep")

t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)


#86 lecture
#Walrus Operator
a=True
print(a:=False)     #Walrus Operator


numbers=[1,2,3,4,5,6]
while(n:=len(numbers))>0:
    print(numbers.pop())
    
#Example 3
foods =list()
while(food:=input("Enter what food you like :"))!="quit":
    foods.append(food)


