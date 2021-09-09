from test.utils import get_random_string


class Post:

    def __init__(self, title=None, content=None, slug= None, author=None):
        self.title = title
        self.content = content
        self.author = author
        self.slug = slug

    def __str__(self):
        return self.title

    def create_post(self, title=None, content=None, slug= None):
        rnd = get_random_string()
        if title is not None:
            title = "title_" + rnd
        if content is not None:
            content = "content_" + rnd
        if slug is None:
            slug = rnd
        post = Post(title, content, slug)
        post.create_with_endpoint()

    def get_post(self, slug):
        pass

    def create_with_endpoint(self):
        pass

