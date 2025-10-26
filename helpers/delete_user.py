import allure
import requests
from data import ApiPath


def delete_user(user_id):
    with allure.step("Отправляем запрос на удаление курьера"):
        response = requests.delete(ApiPath.COURIER + f"/{user_id}")
    with allure.step("Проверка кода ответа"):
        assert response.status_code == 200
