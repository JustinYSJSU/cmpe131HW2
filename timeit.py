#keeps track of the amount of time it takes a function to run
import time

#example of a decorator in python
def calculate_time(function):
 def wrapper():
  currentTime = time.time()
  print(f"The current time is {currentTime}")
  function()
  afterTime = time.time()
  print(f"The time after running function is {afterTime}")
  totalTime = afterTime - currentTime  
  print(f"Total time {totalTime}")
 return wrapper

@calculate_time
def timeMe():
 print("FUNCTION RUNNING")

#call sub function to get the decorator to run
timeMe()
