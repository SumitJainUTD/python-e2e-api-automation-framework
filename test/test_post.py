import pytest
import requests
from test.data_provider import get_data_json
from test.conftest import get_env, get_token_for_user, test_posts as all_test_posts
from main.post import Post
from main.utils.configuration import Configuration


# def test_get_all_posts():
#     response = requests.get("http://127.0.0.1:3000/api/health/")
#     print(response.status_code)
#     print(response.text)
#     assert response.ok

def get_data_create_post(category):
    data = get_data_json("positive")
    PostApiTest.posts = data.get('posts')
    return data.get('test_data')


class PostApiTest:
    posts = []

    @pytest.mark.parametrize('test_data', get_data_create_post(""))
    def test_create_post(self, test_data):
        env = get_env()
        author = test_data.get('user')
        title = test_data.get('title')
        content = test_data.get('content')
        token = get_token_for_user(user=author, refresh=False)
        response = Post.create_post(title=title, content=content, token=token, env=env)
        print(response.status_code)
        print(response.text)
        assert response.ok
