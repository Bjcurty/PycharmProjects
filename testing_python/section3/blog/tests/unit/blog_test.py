from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test", "Test Author")
        b2 = Blog("Test", "Test Author", posts=["OOF"])
        b3 = Blog("Test", "Test Author", posts=["Big", "OOF"])

        self.assertEqual("Test", b.title)
        self.assertEqual("Test Author", b.author)
        self.assertListEqual([], b.posts)

        self.assertEqual("Test", b2.title)
        self.assertEqual("Test Author", b2.author)
        self.assertListEqual(["OOF"], b2.posts)

        self.assertEqual("Test", b3.title)
        self.assertEqual("Test Author", b3.author)
        self.assertListEqual(["Big", "OOF"], b3.posts)

    def test_repr(self):
        b = Blog("Test", "Test Author")
        b2 = Blog("Test", "Test Author", posts=["OOF"])
        expected = f"<Test by Test Author (0 posts)>"
        expected2 = f"<Test by Test Author (1 post)>"

        self.assertEqual(expected, b.__repr__())
        self.assertEqual(expected2, b2.__repr__())

    def test_repr_multiple_posts(self):
        b = Blog("Test", "Test Author", posts=["OOF"])
        b2 = Blog("Test", "Test Author", posts=["Big", "OOF"])
        expected = f"<Test by Test Author (1 post)>"
        expected2 = f"<Test by Test Author (2 posts)>"

        self.assertEqual(expected, b.__repr__())
        self.assertEqual(expected2, b2.__repr__())

    # Not a unit test because it depends on Post. It tests both Blog and Post
    # def test_create_post_in_blog(self):
    #     b = Blog("Test", "Test Author")
    #     b.create_post("Test Post", "Test Content")
    #
    #     self.assertEqual(len(b.posts), 1)
    #     self.assertEqual(b.posts[0].title, "Test Post")
    #     self.assertEqual(b.posts[0].content, "Test Content")

    # Taking to integration testing
    # def test_json(self):
    #     b = Blog("Test", "Test Author")
    #     b2 = Blog("Test", "Test Author", posts=["OOF"])
    #     expected = {"title": "Test", "author": "Test Author", "posts": []}
    #     expected2 = {"title": "Test", "author": "Test Author", "posts": ["OOF"]}
    #
    #     self.assertDictEqual(expected, b.json())
    #     self.assertDictEqual(expected2, b2.json())
