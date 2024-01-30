#Math-caseusage simple example
x = 4
match x:
    case 0:
        print("This is zero")
    case 1:
        print("This is one")
    case _:
        print("Default case")
        
#Example 2

z = 6
match z:
    case 0:
        print("This is zero")
    case 4:
        print("This is one")
        
    case _ if z!=90:
        print(z, "is not 90")
    case _ if z!=80:
        print(z, "z is not 80")
    case _:
        print(z)