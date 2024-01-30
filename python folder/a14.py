#if usage
a=int(input("Enter Your Age:"))
print("Your age is:",a)

if(a>18):
    print("You can vote")
else:
    print("You cannot vote")
    
    # conditional operators
    # >,<.>=,<=,==,!=
    
#if-else
a=280;
b=250;
if(a>=b):
    print("Good")
else:
    print("Bye")
    
#if-else-elif
num=int(input("Enter the value of number :"))
if(num<0):
    print("Number is positive")
elif(num==0):
    print("The Number is zero")
elif(num==999):
    print("The Number is Special:")
else:
    print("THe Number is Positive")
print("Good day")   

#nested if-elif-else
num=20
if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<10):
        print("The Number is less than 10")
    elif(num>10 and num<20):
        print("The Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("The Number is zerp")
        
 
    
    
    