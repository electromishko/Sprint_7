import allure
import requests
from data import ApiPath


class TestOrdersList:
    def test_successful_get_orders(self):
        with allure.step("Получаем список заказов"):
            response = requests.get(ApiPath.ORDER)

        with allure.step("Проверка кода и тела ответа"):
            assert response.status_code == 200
            assert len(response.json()["orders"]) > 0
