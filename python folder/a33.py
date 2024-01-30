#dictionaries in python
#dictionaries are ordered collection of data items .
#dictionary items are key-value pairs that are separated by commas and enclosed with curly brackets

dict ={"Abhi":"Hello","Span":"Good"}
print(dict["Abhi"])

#Example 2
info ={'name':'karan','age':'18','eligible':True}
print(info)
print(info['name'])
print(info.get('name'))
print(info.keys())
print(info.values())

for key in info.keys():
    print(info[key])
    
abhi ={'name':'Abhi','gender':'Male','Div':'A'}
print(abhi.items())
for key,value in abhi.items():
    print(f"The value of corresponding to the key {key} is {value}")
    
#Lecture 34 dictionary methods
info2 ={'name':'Abhi','age':'20','eligible':True}
print(info2)
info2.update({'age':19}) #1
info2.update({'DOB':2004})
print(info2)
a={1:'hello',2:'ok'}
a.clear()
print(a)
empt={}
print(empt)

#pop()
info3 ={'name':'Abhi','age':'20','eligible':True}
info3.pop('name')
print(info3)

info4 ={'name':'Abhi','age':'20','eligible':True}
info4.popitem() #removes the last-key value pair from the dictionary
print(info4)

#35 lecture number
#for loop with else in python
#Example 1
for i in range(5):
    print(i)
else:
    print("Sorry i")        #else executes when the loop completes it will not print when it breaks

#Example2:
for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("Else loop not executes because of break statement")  

