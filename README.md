# What is decorators in python?
Python decorators allow you to modify or extend the behavior of functions and methods without changing their actual code. When you use a Python decorator, you wrap a function with another function, which takes the original function as an argument and returns its modified version. This technique provides a simple way to implement higher-order functions in Python, enhancing code reusability and readability.
# How they works?
## Practical use cases for decorators:
Iinclude logging, enforcing access control, caching results, and measuring execution time.
## Custom decorators:
Custom decorators are written by defining a function that takes another function as an argument, defines a nested wrapper function, and returns the wrapper.
## Multiple decorators:
They can be applied to a single function by stacking them before the function definition.
The order of decorators impacts the final output since each decorator wraps the next, influencing the behavior of the decorated function.
