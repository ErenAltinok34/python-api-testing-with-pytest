import requests

def test_get_users_status_code():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    assert response.status_code == 200

def test_get_users_response_json():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10  # JSONPlaceholder'da 10 kullanıcı var
    assert "name" in data[0]
    assert "email" in data[0]
    assert "address" in data[0]
