class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"<Post: {self.title}, having content: {self.content}>"

    def json(self):
        return {
            "title": self.title,
            # The trailing comma here is optional, easier to add more later to dictionary
            "content": self.content,
        }
