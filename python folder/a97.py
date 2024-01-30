#97 lecture
#Multithreading
#Multithreading in Python allows you to execute multiple threads
#(smaller units of a process) concurrently within a single process.
# Each thread can perform a specific task independently, and they share
# the same memory space, making communication between threads relatively 
# easy. Multithreading is useful when dealing with tasks that involve
# waiting for I/O operations, as it allows the program to make efficient
# use of the CPU by switching between threads while waiting for I/O
import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(2)

def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")
        time.sleep(2)

# Create two threads, one for each function
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish before proceeding
thread1.join()
thread2.join()

print("Both threads have finished.")
