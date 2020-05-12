class Person:
    # init is known as a magic method because python will perform it automatically
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Magic method when object is being turned into a string
    def __str__(self):
        return f"Person {self.name}, {self.age} years old."

    # purpose of this method is to be unambiguous so that the object can be recreated
    # Used in debugger
    def __repr__(self):
        return f"<Person({self.name}, {self.age}>"

bob = Person("Bob", 35)
# Python prints out a string where the object is located at
print(bob)
