#Exception example 1
a=input("Enter a number:")
print(f"Multiplication of table{a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")
except:
    print("Invalid input")
    
print("Some important lines of code")
print("End of Program")

#Example2:
try:
    num=int(input("Enter an integer:"))
    a =[6,3]
    print(a[num])
except ValueError:
    print("Number Entered is not an integer")
except IndexError:
    print("Index Error")
    
#Lecture 37
#finaly usage
try:
    l=[2,2,3,4,5,6]
    i=int(input("Enter the index:"))
    print(l[i])
except:
    print("Some error occurred:")
finally:
    print("I am always executed:")
    
def func():
    try:
        l=[2,2,3,4,5,6]
        i=int(input("Enter the index:"))
        print(l[i])
    except:
        print("Some error occurred:")
    finally:
        print("I am always executed:")
func()