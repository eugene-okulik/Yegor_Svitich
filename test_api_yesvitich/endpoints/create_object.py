import requests
import allure

from endpoints.endpoint import Endpoint

class CreateObject(Endpoint):
    @allure.step("Отправить POST-запрос на создание объекта")
    def create_object(self, payload):
        self.response = requests.post(
            f"{self.base_url}/object",
            json=payload,
            headers=self.headers
        )
        self.response_json = self.response.json()
        return self.response
