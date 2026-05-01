import pytest
import requests


@pytest.fixture(scope="session")
def session_msg():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture
def each_test_msg():
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture
def new_object():
    body = {
        "name": "Yegor's object",
        "data": {
            "name": "Yegor",
            "surname": "Svitich",
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    print(f'\n{object_id}')
    yield object_id
    print('Deleting the object...')
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


def test_get_all_objects(session_msg, each_test_msg):
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    print(response)


def test_get_one_object(new_object, session_msg, each_test_msg):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object}').json()
    assert response['id'] == new_object


def test_put_an_object(new_object, session_msg, each_test_msg):
    body = {
        "name": "Yegor's object (updated)",
        "data": {
            "name": "Yegor (updated)",
            "surname": "Svitich (updated)",
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == "Yegor's object (updated)", 'Name (obj) is incorrect'
    print(response)


@pytest.mark.medium
def test_patch_an_object(new_object, session_msg, each_test_msg):
    body = {
        "data": {
            "name": "Yuri",
            "surname": "Svitich",
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_object}',
        json=body,
        headers=headers
    ).json()
    assert response['data']['name'] == "Yuri", 'Name is incorrect'
    print(response)


def test_delete_an_object(new_object, session_msg, each_test_msg):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object}')
    if response.status_code == 200:
        print(response)
    else:
        print("Invalid response format or empty content")


@pytest.mark.critical
@pytest.mark.parametrize("name, data", [
    ("Yegor's object 1", {"Yegor 1": "Svitich 1"}),
    ("Yegor's object 2", {"Yegor 2": "Svitich 2"}),
    ("Yegor's object 3", {"Yegor 3": "Svitich 3"})
])
def test_create_an_object(session_msg, each_test_msg, name, data):
    body = {
        "name": name,
        "data": data
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == name, 'Name (obj) is incorrect'
    print(response.json())
    requests.delete(f"http://objapi.course.qa-practice.com/object/{response.json()['id']}")
