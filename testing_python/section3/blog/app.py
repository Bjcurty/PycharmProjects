from blog import Blog


MENU_PROMPT = "Enter 'c' to create a blog, 'l' to list blogs, 'r' to read one, 'p' to create a post, or 'q' to quit. "
POST_TEMPLATE = """
--- {} ---

{}

"""

blogs = dict()  # blog_name : Blog object

def menu():
    # Show the user available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


# method is a function inside of a class, functions are not in the class
def print_blogs():
    # Print the available blogs
    # This gives a tuples of lists from the dict to go through
    # [(blog_name, Blog), (blog_name, Blog)]
    for key, blog in blogs.items():
        print(f"- {blog}")


def ask_create_blog():
    # Ask user for title and name, create new blog w/title and name in blogs dict
    title = input("Input a title for the blog: ")
    name = input("Input your name: ")

    blogs[title] = Blog(title, name)


def ask_read_blog():
    title = input("What blog title are you looking for? ")

    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_name = input("Which blog would you like to add a post? ")
    title = input("Input a title for your post: ")
    content = input("Input the content for your post: ")

    blogs[blog_name].create_post(title, content)




