import requests
import allure

from endpoints.endpoint import Endpoint

class PatchObject(Endpoint):
    @allure.step("Отправить PATCH-запрос для частичного обновления объекта")
    def patch_object(self, object_id, payload):
        self.response = requests.patch(
            f"{self.base_url}/object/{object_id}",
            json=payload,
            headers=self.headers
        )
        self.response_json = self.response.json()
        return self.response
