# Composition is a counterpart to inheritance that is used to build out classes that use others
# More used than inheritance
class BookShelf:
    def __init__(self, *books):
    # def __init__(self, quantity):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


# shelf = BookShelf(300)

# print(shelf)

# Even though we can inherit from BookShelf, it's probably not best to do so as the quantity variable isn't
# needed. This is why inheritance is not so useful.
# Composition is for the thought: 'A BookShelf is composed of many books'
# class Book(BookShelf):
class Book:
    # def __init__(self, name, quantity):
    def __init__(self, name):
        # super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)
print(shelf)