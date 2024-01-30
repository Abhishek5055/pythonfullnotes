#Lecture 98 Multi Processing
# Multiprocessing in Python allows you to create multiple processes, 
# each with its own Python interpreter and memory space.
# Unlike multithreading, multiprocessing can take full advantage of 
# multiple CPU cores and allows true parallelism for CPU-bound tasks. 
# Each process runs independently, which can significantly speed up 
# the execution of CPU-intensive operations.
import multiprocessing

def square(number):
    result = number * number
    print(f"The square of {number} is {result}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Create a pool of worker processes
    pool = multiprocessing.Pool()

    # Map the square function to the list of numbers
    pool.map(square, numbers)

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()

    print("All processes have finished.")