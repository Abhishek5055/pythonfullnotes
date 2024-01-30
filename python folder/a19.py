# usage of break statement
for i in range(12):
    if(i==10):
        break
    print("5 X",i+1,"=", 5*(i+1))
        
print("The break statement breaks the loop")

#Example 2
for i in range(6):
    if(i==4):
        print("Skip the Statement")
        continue
    print("5 X",i," = ",5*i)
    
    
#Example 3 for loop all 3 usage
for i in range(1,101,1):
    print(i,end=' ')
    if(i==50):
        break
    else:
        print("Good day")