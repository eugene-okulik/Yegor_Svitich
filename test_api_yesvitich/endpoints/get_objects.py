import requests
import allure

from endpoints.endpoint import Endpoint

class GetObjects(Endpoint):

    @allure.step("Отправить GET-запрос на получение всех объектов")
    def get_all_objects(self):
        self.response = requests.get(f"{self.base_url}/object")
        self.response_json = self.response.json()
        return self.response

    @allure.step("Отправить GET-запрос на получение объекта по ID")
    def get_object_by_id(self, object_id):
        self.response = requests.get(f"{self.base_url}/object/{object_id}")
        self.response_json = self.response.json()
        return self.response
