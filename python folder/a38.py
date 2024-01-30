# #38 lecture
# #in python we can use a custome error by raise
# a=int(input("Enter the value between 5 and 9:"))

# if(a<5 or a>9):
#     raise ValueError("value should be between 5 and 9")

#39 lecture
#exercise 3 kbc 

questions = [
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language was used to create whatsapp?", "Python", "Erlang", "JavaScript",
    "Php", "None", 2
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")

#40 lecture
#Excercise 3 decode
