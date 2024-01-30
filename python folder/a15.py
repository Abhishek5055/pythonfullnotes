import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
def greet():
    current_hour = int(time.strftime("%H"))
    
    if current_hour >= 5 and current_hour < 12:
        print("Good Morning!")
    elif current_hour >= 12 and current_hour < 18:
        print("Good Afternoon!")
    else:
        print("Good Evening!")
        
greet()

