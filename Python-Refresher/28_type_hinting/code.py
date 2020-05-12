from typing import List

# This is a way to tell what the parameter should be and what the function will return
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


print(list_avg([123]))


# class Book:
#     def __init__(self, name: str, page_count: int):
#         self.name = name
#         self.page_count = page_count


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g"

    @classmethod
    # The "Book" is how to show the current class will be returned. Can't use Book
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, Book.TYPES[1], page_weight)