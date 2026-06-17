def myDecorator(func):   #Decorator
  def nestedFunc():   # Any name it is for decoration
       print("Before excuting the function")  # Message from decorator
       func()   # Excute function
       print("After excuting the function")   # Message from decorator
  return nestedFunc  # return all data

@myDecorator
def sayHello():
   print("Hello")

@myDecorator
def sayHowAreYou():
   print("How are you?")

sayHello()
sayHowAreYou()
