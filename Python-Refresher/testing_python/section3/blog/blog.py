from typing import List, Optional
from post import Post


class Blog:
    def __init__(self, title: str, author: str, posts=None):
        self.title = title
        self.author = author
        self.posts = posts or []

    def __repr__(self):
        return f"<{self.title} by {self.author} ({len(self.posts)} " \
               f"post{'s' if len(self.posts) != 1 else ''})>"

    def create_post(self, title, content):
        self.posts.append(Post(title, content))
        return

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts],
        }
