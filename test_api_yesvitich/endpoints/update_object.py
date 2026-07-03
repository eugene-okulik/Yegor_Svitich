import requests
import allure

from endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):
    @allure.step("Отправить PUT-запрос для полного обновления объекта")
    def update_object(self, object_id, payload):
        self.response = requests.put(
            f"{self.base_url}/object/{object_id}",
            json=payload,
            headers=self.headers
        )
        self.response_json = self.response.json()
        return self.response
