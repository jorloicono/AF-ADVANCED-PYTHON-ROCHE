# # Concurrency and Parallelism in Python

# Concurrency and parallelism are two important concepts for managing multiple tasks.
# - **Concurrency** is about managing multiple tasks at the same time but not necessarily simultaneously.
# - **Parallelism** is about executing multiple tasks simultaneously.

# Python provides various ways to handle concurrency and parallelism, including threads and processes.

# ## 1. Threads

# Threads are a way to run multiple threads (smaller units of a process) concurrently within the same process.
# Python's `threading` module provides a way to work with threads.

# ### Example: Using Threads

import threading
import time

# Function to be run in a thread
def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

# Function to be run in a thread
def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")
        time.sleep(1)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Both threads have finished execution.")

# Note: Threads run concurrently, so the output from both functions interleaves.

# ## 2. Processes

# Processes are separate instances of the Python interpreter and have their own memory space.
# The `multiprocessing` module allows us to work with processes, providing true parallelism.

# ### Example: Using Processes

from multiprocessing import Process
import os

# Function to be run in a process
def print_process_info():
    print(f"Process ID: {os.getpid()}")
    for i in range(5):
        print(f"Process {os.getpid()} - Count: {i}")
        time.sleep(1)

# Create processes
process1 = Process(target=print_process_info)
process2 = Process(target=print_process_info)

# Start processes
process1.start()
process2.start()

# Wait for processes to complete
process1.join()
process2.join()

print("Both processes have finished execution.")

# Note: Processes run in parallel, so they do not share memory and run independently.

# ## 3. Inter-Process Communication (IPC)

# When working with processes, they do not share memory directly. 
# Inter-Process Communication (IPC) allows processes to communicate and share data.

# Python's `multiprocessing` module provides several mechanisms for IPC, such as `Queue`, `Pipe`, and `Value`.

# ### Example: Using Queue for IPC

from multiprocessing import Process, Queue

# Function to put data in the queue
def producer(queue):
    for item in range(5):
        queue.put(item)
        print(f"Produced: {item}")
        time.sleep(1)

# Function to get data from the queue
def consumer(queue):
    while True:
        item = queue.get()
        if item is None:  # Sentinel value to indicate end of data
            break
        print(f"Consumed: {item}")

# Create a queue
queue = Queue()

# Create processes
producer_process = Process(target=producer, args=(queue,))
consumer_process = Process(target=consumer, args=(queue,))

# Start processes
producer_process.start()
consumer_process.start()

# Wait for producer to finish
producer_process.join()
# Put a sentinel value to signal the consumer process to stop
queue.put(None)
# Wait for consumer to finish
consumer_process.join()

print("Producer and consumer processes have finished execution.")

# Note: The Queue allows safe exchange of data between processes.
