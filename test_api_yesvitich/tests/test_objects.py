import allure
import pytest
from endpoints.get_objects import GetObjects
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.patch_object import PatchObject
from endpoints.delete_object import DeleteObject

from data.payloads import update_object_payload, patch_object_payload, CREATE_OBJECT_DATA


@allure.feature('Objects Feature')
@allure.story('Tests for GET-methods')
def test_get_all_objects():
    get_objects_endpoint = GetObjects()
    get_objects_endpoint.get_all_objects()
    get_objects_endpoint.check_status_code_is_(200)


@allure.feature('Objects Feature')
@allure.story('Tests for GET-methods')
def test_get_one_object(new_object):
    get_objects_endpoint = GetObjects()
    get_objects_endpoint.get_object_by_id(new_object)
    get_objects_endpoint.check_status_code_is_(200)
    get_objects_endpoint.check_response_field('id', new_object)


@allure.feature('Objects Feature')
@allure.story('Tests for POST-, DELETE-methods')
@pytest.mark.critical
@pytest.mark.parametrize("name, data", CREATE_OBJECT_DATA)
def test_create_an_object(name, data):
    create_object_endpoint = CreateObject()
    delete_object_endpoint = DeleteObject()
    payload = {
        "name": name,
        "data": data
    }

    create_object_endpoint.create_object(payload)
    create_object_endpoint.check_status_code_is_(200)
    create_object_endpoint.check_response_field('name', name)

    created_object_id = create_object_endpoint.response_json['id']
    delete_object_endpoint.delete_object(created_object_id)


@allure.feature('Objects Feature')
@allure.story('Tests for PUT-, PATCH-methods')
def test_put_an_object(new_object):
    update_object_endpoint = UpdateObject()
    update_object_endpoint.update_object(new_object, update_object_payload())
    update_object_endpoint.check_status_code_is_(200)
    update_object_endpoint.check_response_field('name', "Yegor's object (updated)")


@allure.feature('Objects Feature')
@allure.story('Tests for PUT-, PATCH-methods')
@pytest.mark.medium
def test_patch_an_object(new_object):
    patch_object_endpoint = PatchObject()
    patch_object_endpoint.patch_object(new_object, patch_object_payload())
    patch_object_endpoint.check_status_code_is_(200)


@allure.feature('Objects Feature')
@allure.story('Tests for POST-, DELETE-methods')
def test_delete_an_object(new_object):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_object(new_object)
    delete_object_endpoint.check_status_code_is_(200)
