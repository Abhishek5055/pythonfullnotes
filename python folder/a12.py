fruit="Mango"
len1 =len(fruit)
print(len1)
print(fruit[0:4])

#Negative sllicing
print(fruit[0:-3]) #it is equivalent to len(fruit)-value
print(fruit[-3:-1])  #it will do 5-3:5-1===2:4 ===ng

nm="Abhis"
print(nm[-4:-2])


#13 th day of code
#Strings are immutable ,in this below it makes copy then changes here

a="Abhi"
print(a.upper())
print(a.lower())

#rstrip() usage it will remove the trailing character

b="Abcd!!!!!!!"
print(b.rstrip("!")) #it will remove only after letters not before letters

#usage of replace()

c="Abhishek!!!!"
print(c.replace("h","Cd"))

#split function
e="Silver Lady"
print(e.split(" "))

#usage of capitalise function

heading="good morning to one and all"
print(heading.capitalize())

#usage of center()function
str1="Welcome to the console"
print(len(str1))
print(len(str1.center(50)))

#count()function
a="Abhi!!!!!Abhi"
print(a.count("Abhi"))

#endswith()function usage
str1="Welcome to the Console  !!!!!!"
print(str1.endswith("!!!"))

#or it will  help to identify the letter present in between these indexes
str1="Welcome to the Console!!!"
print(str1.endswith("to", 4, 10))

#find()function usage
str2="He's a good person what is the problem  with  you"
print(str2.find("is"))

#isalnum()usage
str3="WelcometotheMyword1233"
print(str3.isalnum())

#isalpha()usage
str4="WelcometotheMyword"
print(str4.isalpha())

#islower()
str5="hello world"
print(str5.islower())


#isprintable()
str6="We wish you a Happy Marriage"
print(str6.isprintable())

#example 2 for printable() function
str7="We wish you a Happy Marriage\n"
print(str7 .isprintable())

#isspace() function usage
str8="      "
print(str8.isspace())   #or another example
str9="          good"
print(str9.isspace())

#usage of istitle()
str10="Good Morning"
print(str10.istitle())  #2nd Example
str11="good"
print(str11.istitle())


#isupper()
str11="ABHI"
print(str11.isupper())

#startswith()
str12="ABHI"
print(str12.startswith("ABHI"))

#swapcase()
str13="Abhi is"
print(str13.swapcase())

#title()
str14="Abhi is a good boy"
print(str14.title())