#a class with a double decorator

def doubler(func):
 def wrapper():
  print("Before")
  func()
  func()
  print("After")
 return wrapper

@doubler
def twoTime():
 print("This is part of a double call")

twoTime()
