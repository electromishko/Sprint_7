import pytest
import allure
import requests
from data import ApiPath, ApiErrors


class TestCourierLogin:
    def test_successful_login_courier(self, create_courier):
        with allure.step("Формирование тела запроса"):
            payload = {
                "login": create_courier.login,
                "password": create_courier.password
            }

        with allure.step("Отправляем запрос на логин"):
            response = requests.post(ApiPath.LOGIN, data=payload)
        
        with allure.step("Проверка кода и тела ответа"):
            create_courier.user_id = response.json()["id"]
            assert response.status_code == 200
            assert response.json()["id"] > 0

    @pytest.mark.xfail(reason="API возвращает 504 вместо ожидаемого 400 - баг сервера")
    def test_unsuccessful_login_courier_without_password_field(self, create_courier):
        with allure.step("Формирование тела запроса"):
            payload = {
                "login": create_courier.login
            }
        
        with allure.step("Отправляем запрос на логин"):
            response = requests.post(ApiPath.LOGIN, data=payload)
        
        with allure.step("Проверка кода и тела ответа"):
            assert response.status_code == 400
            assert response.json()["message"] == ApiErrors.LOGIN_ERROR_WITHOUT_FILEDS

    def test_unsuccessful_login_courier_without_login_field(self, create_courier):
        with allure.step("Формирование тела запроса"):
            payload = {
                "password": create_courier.password
            }
        
        with allure.step("Отправляем запрос на логин"):
            response = requests.post(ApiPath.LOGIN, data=payload)
        
        with allure.step("Проверка кода и тела ответа"):
            assert response.status_code == 400
            assert response.json()["message"] == ApiErrors.LOGIN_ERROR_WITHOUT_FILEDS

    def test_unsuccessful_login_courier_with_incorrect_password(self, create_courier):
        with allure.step("Формирование тела запроса"):
            payload = {
                "login": create_courier.login,
                "password": "123"
            }

        with allure.step("Отправляем запрос на логин"):
            response = requests.post(ApiPath.LOGIN, data=payload)
        
        with allure.step("Проверка кода и тела ответа"):
            assert response.status_code == 404
            assert response.json()["message"] == ApiErrors.LOGIN_ERROR

    def test_unsuccessful_login_courier_with_incorrect_login(self, create_courier):
        with allure.step("Формирование тела запроса"):
            payload = {
                "login": "123",
                "password": create_courier.password
            }

        with allure.step("Отправляем запрос на логин"):
            response = requests.post(ApiPath.LOGIN, data=payload)
        
        with allure.step("Проверка кода и тела ответа"):
            assert response.status_code == 404
            assert response.json()["message"] == ApiErrors.LOGIN_ERROR
