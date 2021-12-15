from test.utils import get_random_string
from .api_client import ApiClient
from .utils.configuration import Configuration


class Post:

    def __init__(self, api_client=None, env=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.config = Configuration(env)

    def __init__(self, title=None, content=None, slug=None, author=None, env=None):
        self.title = title
        self.content = content
        self.author = author
        self.slug = slug
        Post(env)

    def __str__(self):
        return self.title

    def create_post(self, title=None, content=None, token=None, slug=None, env='qa'):
        rnd = get_random_string()
        if title is not None:
            title = "title_" + rnd
        if content is not None:
            content = "content_" + rnd
        if slug is None:
            slug = rnd
        post = Post(title, content, slug, env)
        return post.create_with_endpoint()

    def get_post(self, slug):
        pass

    def create_with_endpoint(self, title, content, token):
        headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
        body = {
            'title': title,
            'content': content

        }
        config = self.config
        url = config.base_uri + config.post_uri + config.create_post_uri
        response = self.api_client.call_api(self, url=url, body=body, headers=headers)
