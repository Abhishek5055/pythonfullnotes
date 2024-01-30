#loops
#for loop
name = "Abhishek"
for i in name:
    print(i)
    
#Example 2
#usage of for loop in lists

colors = ["Blue","Red","Pink","Yellow"]
for color in colors:
    print(color)    #to iterate colr like character wise
    for i in color:
        print(i)
        
#usage of range() function in for loop
for j in range(0,5):    #it will print(0 to 4)
    print(j)
    
for z in range(0,5):
    print(z+1)

#for loop with step 
for g in  range(1,34,6):    #where last parameter used to increment the value by +6 times when the loop runs
    print(g)
