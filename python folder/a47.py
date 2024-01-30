# #Excercise 4
# st=input("Enter your message:")
# words=st.split(" ")
# coding=input("1 for coding or 0 for decoding")
# coding=True if(coding =="1") else False
# print(coding)

# if(coding):
#     nwords=[]
#     for word in words:
#         if(len(word)>=3):
#             r1="dsf"
#             r2="jkr"
#             stnew =r1+word[1:]+word[0]+r2
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#         print(" ".join(nwords))
# else:
#     nwords=[]
#     for word in words:
#         if(len(word)>=3):
#             stnew=word[3:-3]
#             stnew=stnew[-1]+stnew[:-1]
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#         print(" ".join(nwords))
        
#48 lecture
# x=4
# print(x)
# def hello():
#     x=5
#     print(f"the local x is{x}")
#     print("Hello Abhi")
# hello()
# print(f"The Global x is{x}")

# #Example 2
# z=4  #global variable
# def ab():
#     global z
#     z=5
# ab()
# print(z)

# #49 lecture
# #f=open('myfile.text2','w') Here it will create a file if not exists
#Reading a file
# f=open('myfile.text','r')       #it will open file in read mode
# text=f.read()
# print(text)
# f.close()

#writing in a file
# f=open('myfile2.txt','w')
# f.write('hello World!')
# f.close()

#Appending a file
# f=open('myfile2.txt','a')
# f.write("Good Morning")
# f.close()

#with statement
with open('myfile.text','a') as f:
    f.write('Hey I am inside with')