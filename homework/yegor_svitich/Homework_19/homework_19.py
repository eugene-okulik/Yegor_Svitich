import requests


def all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    print(response)


def one_object():
    object_id = new_object()
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}').json()
    assert response['id'] == object_id


def create_an_object():
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
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == "Yegor's object", 'Name is incorrect'
    print(response.json())


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
    return response.json()['id']


def clear(object_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


def put_an_object():
    object_id = new_object()
    body = {
        "name": "Yegor's object (updated)",
        "data": {
            "name": "Yegor (updated)",
            "surname": "Svitich (updated)",
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == "Yegor's object (updated)"
    print(response)
    clear(object_id)


def patch_an_object():
    object_id = new_object()
    body = {
        "data": {
            "name": "Yuri",
            "surname": "Svitich",
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    ).json()
    print(response)
    clear(object_id)


def delete_an_object():
    object_id = new_object()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    if response.status_code == 200:
        print(response)
    else:
        print("Invalid response format or empty content")


delete_an_object()
