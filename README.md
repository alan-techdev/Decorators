# What is decorator in python? 🤔
It is a function that takes another function, it extends the behavior of functions and methods without changing their actual code. When you use a Python decorator, you wrap a function with another function, which takes the original function as an argument and returns its modified version. This technique provides a simple way to implement higher-order functions in Python, enhancing code reusability and readability.

### simple idea 💡:
Imagine you have a gift 🎁, the gift it self is the function.
The wrapping paper and the ribbon 🎀 are the decorator.
When you add a decorator, you didn't change the gift inside, but you add something new around it, like colorful or a bow.
  
### Practical use cases for decorators:
They are often used in scenarios such as logging, authentication and memorization, enforcing access control, caching results, and measuring execution time.

* TODO : we need to find examples from open source libraries  like DJANGO, PYTEST or ??? ....

## How they works? 📌
Define the decorator first, then apply it with @decorator_name above the function.
### Custom decorators:
Custom decorators are written by defining a function that takes another function as an argument, defines a nested wrapper function, and returns the wrapper.

```
def decorator_function(func):
     def inner_func():
         return func() # invoke the input parameter which is a function reference 
     return inner_func # return reference to the inner function
```

### Example:
A basic decorator that uppercases the return value of the decorated function:
```
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Sherin"

print(myfunction())

Code excution result:
HELLO SHERIN
```

By placing ```@changecase``` directly above the function definition, the function ```myfunction``` is being decorated with the ```changecase``` function.
The function ```changecase``` is the decorator, and the function ```myfunction``` is the function that gets decorated.


### Build in decorators:
Python standard runtime library has build in decorators such as 📑
#### 1. @classmethod
@classmethod is used to create a method that works with the class instead of an object instance. A class method receives the class itself as the first argument using cls. It is commonly used to access class variables, create factory methods and perform operations related to the class.

```
class Car:
    brand = "Toyota"

    @classmethod
    def show_brand(cls):
        print(cls.brand)

   Car.show_brand()
```

Output:
Toyota
cls.brand accesses the class variable brand directly using the class method.

### 2. @abstractmethods
Are declared inside an Abstract class without any method definition. This method is meant to be implemented by the base class who implements the parent abstract class. The @abstractmethod decorator provided by abc module is used to implement abstract methods.

```
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
      return self.side**2

square = Square(10)
print(square.area())
```

### 3. @staticmethod
A static method is a method which is bound to the class and NOT the object of the class. It used to create a static method. 

#### Example:
```
class TestClass:
  
  @staticmethod
  def test_static_method():
    print("Hello from static method")
​
TestClass.test_static_method()
```
Output:
Hello from static method

### 4. @atexit.register
The '@atexit.register' decorator is used to call the function when the program is exiting. The functionality is provided by the 'atexit' module. This function can be used to perform the clean-up tasks, before the program exits. Clean-ups are the tasks that have been done in order to release the resources such as opened files or database connections, that were being used during the program execution.

#### Example:
```
import atexit
​
@atexit.register
def person_exit_handler():
  print("Bye, Sherin!")  # The parameters are separated using ', '. 

print("Hello, Sherin!")

Output:

Hello, Sherin!
Bye, Sherin!
```
### 5. @typing.final
The '@final'  decorator from the typing module is used to define the final class or method. Final classes cannot be inherited and in a similar way, final methods cannot be overridden.
```
import typing

class Base:
    @typing.final
    def done(self):
        print("Base")

class Child(Base):
    def done(self):  # Error: Method "done" cannot override final method defined in class "Base" 
        print("Child")

@typing.final
class Test:
    pass

class Other(Test):  # Error: Base class "Test" is marked final and cannot be subclassed
    pass
```

In the above implementation, the @typing.final decorator is used to indicate that a method or class should not be overridden or subclassed, respectively. The Base class has a done() method marked as final using @typing.final. The Child is a subclass of Base that attempts to override the done() method, which raises an error when the code is executed. Similarly, the Test class is marked as final using @typing.final, indicating that it should not be subclassed. The Other class attempts to subclass Leaf, which also raises an error when the code is executed.

Using @typing.final can help prevent unintended changes to critical parts of your code and make it more robust by enforcing constraints on how it can be used.

### 6. @enum.unique
Enumeration or Enum is a set of unique names that have a unique value. They are useful if we want to define a set of constants that have a specific meaning. The '@unique' decorator provided by enum module is used to ensure that enumeration members are unique.
```
from enum import Enum, unique
​
@unique
class Cloths(Enum):
    Small = 1
    Medium = 2
    Large = 3
    Xlarge= 2 # ValueError: duplicate values found in <enum 'Cloths'>: Medium -> Xlarge
```
In the above implementation, an enum class 'Cloths' is defined using the class 'Enum'. The class has 4 members, Small, Medium, Large, and Xlarge, with values of 1,2,3,2 respectively. 

However, because Medium and Xlarge both have the value 2, the @unique decorator raises a ValueError with the message "duplicate values found in <enum 'Cloths'>: Medium -> Xlarge". This error occurs because the @unique decorator ensures that the values of the enumeration members are unique, and in this case, they are not.

### 7. @property
Getters and Setters are used within the class to access or update the value of the object variable within that class. The '@property' decorator is used to define getters and setters for class attributes. 

a code with out using @property:
```
class Student:
    def __init__(self):
        self._grade = 0

    def get_grade(self):
        return self._grade

    def set_grade(self, grade):
        self._grade = grade

student_grade = Student()
student_grade.set_grade(100)
print(student_grade.get_grade())  # الناتج: 100
```
After using @property:
👉 [see](./@property_decorator.py)

```src/buildin/i_singledispatch.py``` <br>
``` @lru_cache ```   ðŸ‘‰ ```src/buildin/j_lru_cache.py``` <br>
``` @l@dataclasses  ```   ðŸ‘‰ ```src/buildin/k_dataclasses.py``` <br>


### Multiple decorators:
ðŸ”¶ï¸ They can be applied to a single function by stacking them before the function definition.
The order of decorators impacts the final output since each decorator wraps the next, influencing the behavior of the decorated function.
ðŸ‘‰ ```src/multiple_decorator_calls.py```

ðŸ”¶ï¸ You can use multiple decorators on one function.

This is done by placing the decorator calls on top of each other.
Decorators are called in the reverse order, starting with the one closest to the function.

* More Example of double decorators
One decorator for upper case, and one for adding a greeting:
```
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Hez"

print(myfunction())
```

### Parametrized Decorators:
Functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function. 
ðŸ‘‰  ```src/parametrized_decorator.py```

### *args and **kwargs: ðŸ–‡
Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.

Example

```
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam1, nam2):
  return "Hello " + nam1 + nam2

print(myfunction("Hez", "Heyv"))

```

### Decorator With Arguments:
Decorators can accept their own arguments by adding another wrapper level.

Example
A decorator factory that takes an argument and transforms the casing based on the argument value.

```
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Hez"

print(myfunction())

```

### Preserving Function Metadata: ðŸ›‘
Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

Example
Normally, a function's name can be returned with the __name__ attribute:

```
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

```

ðŸ‘€ But, when a function is decorated, the metadata of the original function is lost.

Example
Try returning the name from a decorated function and you will not get the same result:

```
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

```

To fix this, Python has a built-in function ðŸ¥³ called ```functools.wraps ``` that can be used to preserve the original function's name and docstring.<br> 
ðŸ‘‰  ```src/metadata_fix.py```
