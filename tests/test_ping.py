import allure
import requests
from data import ApiPath
from data import ApiErrors


class TestPingServer:
    def test_ping_server(self):
        with allure.step("Ping server"):
            response = requests.get(ApiPath.PING)

        with allure.step("Проверка ответа"):
            allure.attach(f"Response Status: {response.status_code}", "Response Status", allure.attachment_type.TEXT)
            allure.attach(f"Response Body: {response.text}", "Response Body", allure.attachment_type.TEXT)

            assert response.status_code == 200
            assert response.text == ApiErrors.PING_OK
