from unittest import TestCase, mock
import builtins
# Mock is a useful tool for testing. return_value can be used to get a desired
# value from a method or function. side_effect can cause an exception to be thrown
# so that it can also be tested
# Mock can be applied as decorator, in context manager or inline
# Decorator: @mock.patch("blog.app.print_blogs", return_value=b"foo\nbar\n")
# spec=True  can be used in mock to make sure it is only able to call functions that exist
# and also maintains proper passed arguments, but it can't introspect.
# autospec=True solves that, but causes attributes to not pass, but if you set
# that to some value in code, it can bypass
# autospec=True, spec_set=True gets past that
from unittest.mock import patch
import app
from blog import Blog
from post import Post


# # This is how to mock as decorator
# class AppTest(TestCase):
#     @mock.patch("builtins.print")
#     def test_print_blogs(self, mock_print):
#         blog = Blog("Test", "Test Author")
#         app.blogs = {"Test": blog}
#         app.print_blogs()
#         builtins.print.assert_called_with("- <Test by Test Author (0 posts)>")


# This is how to mock in context manager. These are good for builtins because they
# are short lived and less likely to cause problems with that built in function opposed
# to decorators
class AppTest(TestCase):
    def test_menu_calls_create_blog(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ('c', "Test Create Blog", "Test Author", 'q')

            app.menu()

            self.assertIsNotNone(app.blogs["Test Create Blog"])

    def test_menu_prints_prompt(self):
        with patch("builtins.input", return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch("app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input", return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}
        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("- <Test by Test Author (0 posts)>")

    def test_ask_create_blog(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Test Author")
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get("Test"))

    def test_ask_read_blog(self):
        blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}
        with patch("builtins.input", return_value="Test"):
            with patch("app.print_posts") as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog("Test", "Test Author")
        blog.create_post("Test Post", "Test Content")
        app.blogs = {"Test": blog}

        with patch("app.print_post") as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post("Post title", "Post content")
        expected_print = """
--- Post title ---

Post content

"""

        with patch("builtins.print") as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)

    def tests_ask_create_post(self):
        blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Test title", "Test content")

            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, "Test title")
            self.assertEqual(blog.posts[0].content, "Test content")

# # This is how to mock inline. These are good for mocking multiple properties or
# # fields.
# class AppTest(TestCase):
#     def setUp(self):
#         self.patcher = patch("builtins.print")
#         self.patcher.start()
#
#     def test_print_blogs(self):
#         blog = Blog("Test", "Test Author")
#         app.blogs = {"Test": blog}
#         app.print_blogs()
#         builtins.print.assert_called_with("- <Test by Test Author (0 posts)>")
#
#     def tearDown(self):
#         self.patcher.stop()
