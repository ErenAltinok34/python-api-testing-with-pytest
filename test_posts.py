import requests

def test_get_posts_status_code():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    assert response.status_code == 200

def test_get_posts_response_json():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "userId" in data[0]
    assert "title" in data[0]