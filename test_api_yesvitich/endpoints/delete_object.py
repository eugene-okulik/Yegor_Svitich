import requests
import allure

from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    @allure.step("Отправить DELETE-запрос на удаление объекта")
    def delete_object(self, object_id):
        self.response = requests.delete(f"{self.base_url}/object/{object_id}")
        return self.response
