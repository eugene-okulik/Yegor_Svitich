import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from data.payloads import create_object_payload


@pytest.fixture()
def new_object():
    create_object_endpoint = CreateObject()
    delete_object_endpoint = DeleteObject()

    payload = create_object_payload()
    create_object_endpoint.create_object(payload)
    object_id = create_object_endpoint.response_json['id']

    yield object_id

    delete_object_endpoint.delete_object(object_id)
