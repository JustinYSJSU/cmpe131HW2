#a class with a double decorator

def doubler(func):
 def wrapper():
  func()
  func()
 return wrapper

@doubler
def twoTime():
 print("This is part of a double call")

twoTime()
