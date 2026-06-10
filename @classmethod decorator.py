# A class method creates an object using a formatted string.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data): # from_string() uses cls() to create and return a new object from the string data.
        n, a = data.split("-")
        return cls(n, int(a))

u = User.from_string("Sherin-36")

print(u.name)
print(u.age)

""" Another example of @classmethod decorator:
clasmethod() function is used directly instead of the @classmethod decorator. """

class Demo:
    name = "Sherin"

    def show(cls):
        print(cls.name)

Demo.show = classmethod(Demo.show)
Demo.show()
