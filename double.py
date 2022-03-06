#a class with a double decorator

def doubler(func):
 def wrapper():
  print("Before")
  func()
  print("After")
  def wrapper2():
   print("Before2")
   func() 
   print("After2")
  return wrapper2
 return wrapper

@doubler
def twoTime():
 print("This is part of a double call")

twoTime()
