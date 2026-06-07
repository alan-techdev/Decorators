# What is decorator in python? 🤔
It is a function that takes another function, it extends the behavior of functions and methods without changing their actual code. When you use a Python decorator, you wrap a function with another function, which takes the original function as an argument and returns its modified version. This technique provides a simple way to implement higher-order functions in Python, enhancing code reusability and readability.

### simple idea 💡:
Imagine you have a gift 🎁, the gift it self is the function.
The wrapping paper and the ribbon 🎀 are the decorator.
When you add a decorator, you didn't change the gift inside, but you add something new around it, like colorful or a bow.

### Practical use cases for decorators:
They are often used in scenarios such as logging, authentication and memorization, enforcing access control, caching results, and measuring execution time.

## How they works? 📌
Define the decorator first, then apply it with @decorator_name above the function.
### Custom decorators:
Custom decorators are written by defining a function that takes another function as an argument, defines a nested wrapper function, and returns the wrapper.

### Example:
A basic decorator that uppercases the return value of the decorated function:
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Sally"

print(myfunction())

Code excution result:
HELLO SALLY

By placing @changecase directly above the function definition, the function myfunction is being decorated with the changecase function.
The function changecase is the decorator, and the function myfunction is the function that gets decorated.

### Multiple decorators:
🔶️ They can be applied to a single function by stacking them before the function definition.
The order of decorators impacts the final output since each decorator wraps the next, influencing the behavior of the decorated function.
see the code 👉 multiple_decorator_calls.py

🔶️ You can use multiple decorators on one function.

This is done by placing the decorator calls on top of each other.
Decorators are called in the reverse order, starting with the one closest to the function.

Example
One decorator for upper case, and one for adding a greeting:

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

### Parametrized Decorators:
Functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function. see 👉  parametrized_decorator.py

### *args and **kwargs: 🖇
Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.

Example

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam1, nam2):
  return "Hello " + nam1 + nam2

print(myfunction("Hez", "Heyv"))

### Decorator With Arguments:
Decorators can accept their own arguments by adding another wrapper level.

Example
A decorator factory that takes an argument and transforms the casing based on the argument value.

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

### Preserving Function Metadata: 🛑
Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

Example
Normally, a function's name can be returned with the __name__ attribute:

def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

👀 But, when a function is decorated, the metadata of the original function is lost.

Example
Try returning the name from a decorated function and you will not get the same result:

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

To fix this, Python has a built-in function 🥳 called functools.wraps that can be used to preserve the original function's name and docstring.

