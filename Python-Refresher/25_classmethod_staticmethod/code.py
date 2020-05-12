# class ClassTest:
#     # all methods that use the class as the first object are called instance methods (self being first)
#     # used for methods that need to use the object
#     def instance_method(self):
#         print(f"Called instance_method of {self}")
#
#     @classmethod
#     # cls is the class itself
#     # used for methods that need to use the class
#     # often used as factories
#     def class_method(cls):
#         print(f"Called class_method of {cls}")
#
#     @staticmethod
#     # a method that doesn't really have any info on the class
#     # just to put methods in classes if they logically belong there
#     def static_method():
#         print("Called static_method.")
#
# # test = ClassTest()
# # test.instance_method()
# # ClassTest.instance_method(test)
#
# # ClassTest is passed in automatically as a parameter
# # ClassTest.class_method()
# ClassTest.static_method()

# factory
class Book:
    # variables become class properties
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g"

    @classmethod
    def hardcover(cls, name, page_weight):
        # cls and Book are interchangeable, but using cls is better when possible
        return cls(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, Book.TYPES[1], page_weight)

# print(Book.TYPES)

# book = Book("Harry Potter", "hardcover", 1500)
book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

# print(book.name)
print(book)
print(light)