from typing import List, Optional
from post import Post


class Blog:
    def __init__(self, title: str, author: str, posts=None):
        self.title = title
        self.author = author
        self.posts = posts or []

    def __repr__(self):
        return f"<Blog with title: {self.title}, author: {self.author} and posts: {self.posts}>"

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": self.posts,
        }

# b = Blog("Test", "Test")
# print( b.__repr__())
