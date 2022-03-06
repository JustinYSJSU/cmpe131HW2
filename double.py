#a class with a double decorator

def doubler(func):
 def wrapper():
  func()
 return wrapper

def doubler2(func):
 def wrapper():
  func()
 return wrapper


@doubler2
@doubler
def twoTime():
 print("This is part of a double call")

twoTime()
