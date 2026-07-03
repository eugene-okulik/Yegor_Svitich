import allure


class Endpoint:
    base_url = "http://objapi.course.qa-practice.com"
    headers = {'Content-Type': 'application/json'}

    response = None
    response_json = None

    @allure.step("Проверить, что статус-код равен {expected_code}")
    def check_status_code_is_(self, expected_code):
        assert self.response.status_code == expected_code

    @allure.step("Проверить значение поля в ответе")
    def check_response_field(self, field_name, expected_value):
        assert self.response_json[field_name] == expected_value
