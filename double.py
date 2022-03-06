#a class with a double decorator

def doubler(func):
 def wrapper():
  print("Before")
  func()
  def wrapper2():
   print("Before 2")
   func()
   print("After 2")
  return wrapper2
  print("After")
 return wrapper

@doubler
def twoTime():
 print("This is part of a double call")

twoTime()
