import allure
import pytest
import requests
from data import ApiPath
from helpers.generators import generate_order_payload


class TestOrderCreate:

    @pytest.mark.parametrize('color',
        [
            [],
            ["BLACK"],
            ["GREY", "BLACK"]
        ])
    def test_successful_create_order(self, color):
        with allure.step("Генерация данных для заказа"):
            payload = generate_order_payload(color=color)

        with allure.step("Отправляем запрос на создание заказа"):
            allure.attach(f"Payload: {payload}", "Request Payload", allure.attachment_type.TEXT)
            allure.attach("Content-Type: application/json", "Headers", allure.attachment_type.TEXT)
            response = requests.post(ApiPath.ORDER, json=payload)

        with allure.step("Проверка кода и тела ответа"):
            allure.attach(f"Response Status: {response.status_code}", "Response Status", allure.attachment_type.TEXT)
            allure.attach(f"Response Body: {response.text}", "Response Body", allure.attachment_type.TEXT)

            assert response.status_code == 201
            assert response.json()["track"] > 0
