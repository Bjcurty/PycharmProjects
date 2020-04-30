from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test", "Test Author")
        b2 = Blog("Test", "Test Author", posts=["OOF"])

        self.assertEqual("Test", b.title)
        self.assertEqual("Test Author", b.author)
        self.assertListEqual([], b.posts)

        self.assertEqual("Test", b2.title)
        self.assertEqual("Test Author", b2.author)
        self.assertListEqual(["OOF"], b2.posts)

    def test_repr(self):
        b = Blog("Test", "Test Author")
        b2 = Blog("Test", "Test Author", posts=["OOF"])
        expected = f"<Blog with title: Test, author: Test Author and posts: []>"
        expected2 = f"<Blog with title: Test, author: Test Author and posts: ['OOF']>"

        self.assertEqual(expected, b.__repr__())
        self.assertEqual(expected2, b2.__repr__())

    def test_create_post(self):
        expected = [Post("Test", "Test Content")]
        b = Blog("Test", "Test Author")
        b.create_post("Test", "Test Content")

        self.assertListEqual(expected, b.posts)

    def test_json(self):
        b = Blog("Test", "Test Author")
        b2 = Blog("Test", "Test Author", posts=["OOF"])
        expected = {"title": "Test", "author": "Test Author", "posts": []}
        expected2 = {"title": "Test", "author": "Test Author", "posts": ["OOF"]}

        self.assertDictEqual(expected, b.json())
        self.assertDictEqual(expected2, b2.json())
