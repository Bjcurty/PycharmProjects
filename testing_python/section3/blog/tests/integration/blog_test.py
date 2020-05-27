from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog("Test", "Test Author")
        b.create_post("Test Post", "Test Content")

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, "Test Post")
        self.assertEqual(b.posts[0].content, "Test Content")

    def test_json(self):
        b = Blog("Test", "Test Author", posts=[Post("Test Post", "Test Content")])
        # b.create_post("Test Post", "Test Content")

        expected = {"title": "Test", "author": "Test Author",
                    "posts": [
                        {"title": "Test Post", "content": "Test Content"}
                    ]}

        self.assertDictEqual(expected, b.json())

    def test_json_with_no_posts(self):
        b = Blog("Test", "Test Author")
        expected = {"title": "Test", "author": "Test Author",
                    "posts": []}

        self.assertDictEqual(expected, b.json())

    def test_json_with_posts(self):
        b = Blog("Test", "Test Author", posts=[Post("Test Post", "Test Content")])
        b2 = Blog("Test", "Test Author")
        b2.create_post("Test Post", "Test Content")
        expected = {"title": "Test", "author": "Test Author",
                    "posts": [{"title": "Test Post", "content": "Test Content"}]}
        expected2 = {"title": "Test", "author": "Test Author",
                     "posts": [{"title": "Test Post", "content": "Test Content"}]}

        self.assertDictEqual(expected, b.json())
        self.assertDictEqual(expected2, b2.json())