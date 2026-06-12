# This example shows how a static method performs a calculation without creating an object of the class.

class Calc:
    @staticmethod
    def add(a, b):  # @staticmethod makes add() independent of class objects
        return a + b
​
res = Calc.add(2, 3) # It directly calls the method using the class name
print(res)
