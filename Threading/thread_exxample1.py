# from threading import Thread
# import threading

# # 


# def display():
#     print("I am running in main thread:", threading.current_thread().getName())

# # Creating and starting multiple threads
# for i in range(10):
#     th = Thread(target=display)  # Pass the function itself, not its result
#     th.start()
from threading import Thread
import threading
import time

# Function to be executed by each thread
from threading import Thread
import threading
import time

# Function to be executed by each thread
def print_numbers(number):
    print(f"Thread {number} started: {threading.current_thread().name}")  # Use 'name' without parentheses
    time.sleep(2)  # Simulate some work by sleeping for 2 seconds
    print(f"Thread {number} finished: {threading.current_thread().name}")  # Use 'name' without parentheses

# Creating multiple threads
threads = []
for i in range(5):
    th = Thread(target=print_numbers, args=(i,))
    threads.append(th)  # Save the thread in a list
    th.start()  # Start the thread

# Waiting for all threads to complete
for th in threads:
    th.join()  # This makes sure the main thread waits for each thread to finish

print("All threads completed.")



import time
from threading import *

# Custom thread class by inheriting from the Thread class
class MyThread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number
    
    # Override the run method
    def run(self):
        print(f"Thread {self.number} started: {self.name}")
        time.sleep(2)
        print(f"Thread {self.number} finished: {self.name}")

# Creating and starting multiple threads
threads = []
for i in range(5):
    th = MyThread(i)  # Create an instance of MyThread
    threads.append(th)
    th.start()  # Start the thread

# Waiting for all threads to finish
for th in threads:
    th.join()

print("All threads completed.")



 