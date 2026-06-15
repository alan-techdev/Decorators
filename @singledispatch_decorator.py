from functools import singledispatch

# define the generic function and the default behavior 
@singledispatch
def add(arg1, arg2):
    print("Unknown Typs")

@add.register(int)
def _(arg1, arg2):
    result = arg1 + arg2
    print(f" Sum of both integer numbers: {arg1} + {arg2} = {result}")
    return result

@add.register(str)
def _(arg1, arg2):
    result = arg1 + arg2
    print(f"Combine of two strings'{arg1}' + '{arg2}' = '{result}'")
    return result

@add.register(list)
def _(arg1, arg2):
    result = arg1 + arg2
    print(f"Combine of two lists: {arg1} + {arg2} = {result}")
    return result
  
add(10, 5)
add("Hello", " Sherin")
add([1, 2, 3], [4, 5])
add(2.5, 1.5)
