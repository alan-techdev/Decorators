# What is decorator in python?
It is a function that takes another function, it extends the behavior of functions and methods without changing their actual code. When you use a Python decorator, you wrap a function with another function, which takes the original function as an argument and returns its modified version. This technique provides a simple way to implement higher-order functions in Python, enhancing code reusability and readability.

### simple idea:
Imagine you have a gift, the gift it self is the function.
The wrapping paper and the ribbon are the decorator.
When you add a decorator, you didn't change the gift inside, but you add something new around it, like colorful paper or a bow.

## Practical use cases for decorators:
They are often used in scenarios such as logging, authentication and memorization, enforcing access control, caching results, and measuring execution time.

## How they works?
Define the decorator first, then apply it with @decorator_name above the function.
## Custom decorators:
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

## Multiple decorators:
They can be applied to a single function by stacking them before the function definition.
The order of decorators impacts the final output since each decorator wraps the next, influencing the behavior of the decorated function.
see the code 
