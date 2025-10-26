import allure
import requests
from helpers.validation import validate_order_response
from helpers.generators import generate_order_payload
from data import ApiPath


class TestOrderGetByNumber:
    def test_successful_get_order_by_number(self):

        with allure.step("Генерация данных для заказа"):
            payload = generate_order_payload()

        with allure.step("Создаем заказ"):
            response = requests.post(ApiPath.ORDER, data=payload)
            assert response.status_code == 201
            assert response.json()["track"] > 0
            order_id = response.json()["track"]

        with allure.step("Получаем заказ по номеру"):
            params = {"t": order_id}
            response_order_by_number = requests.get(ApiPath.TRACK, params=params)

            assert response_order_by_number.status_code == 200
            validate_order_response(response_order_by_number.json())
