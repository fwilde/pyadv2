#!/usr/bin/python3

# importing the sys module to use command-line arguments
import sys
# importing the threading module
import threading
# importing the time module
import time

# define functions for threading
def calc_square(numbers):
   for n in numbers:
      time.sleep(1.1)   #artificial time-delay
      print('Thread-1 (calc_square): ', str(n*n))
        
def calc_cube(numbers):
   for n in numbers:
      time.sleep(1.9)
      print('Thread-2 (calc_cube): ', str(n*n*n))
        
# get command-line argument
if not len(sys.argv) > 1:
    raise ValueError("Expected an integer as command-line argument.")
num = int(sys.argv[1])

# prepare input argument list        
arr = list(range(num))
t = time.time()
# create two threading objects or threads
t1 = threading.Thread(target = calc_square,args=(arr,))
t2 = threading.Thread(target = calc_cube,args=(arr,))

# start the threads by invoking the start() method of the thread object
# running the threads concurrently (for the user they appear to be executed in parallel)
print("Thread-1 start")
t1.start()
print("Thread-2 start")
t2.start()

# the method join waits for the thread to be finished
t1.join()
t2.join()

print("The end.")
