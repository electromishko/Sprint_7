import allure
import requests
from data import ApiPath, ApiErrors
from helpers.user_registration import generate_random_string


class TestCourierCreate:
    def test_successful_create_courier(self):
        with allure.step("Генерируем логин, пароль и имя курьера"):
            login = generate_random_string(10)
            password = generate_random_string(10)
            first_name = generate_random_string(10)
        
        with allure.step("Формирование тела запроса"):
            payload = {
                "login": login,
                "password": password,
                "firstName": first_name
            }

        with allure.step("Отправляем запрос на регистрацию курьера"):
            response = requests.post(ApiPath.COURIER, data=payload)
        
        with allure.step("Проверка кода и тела ответа"):
            assert response.status_code == 201
            assert response.json()["ok"] == True

    def test_unsuccessful_create_courier_with_the_same_data(self):
        with allure.step("Генерируем логин, пароль и имя курьера"):
            login = generate_random_string(10)
            password = generate_random_string(10)
            first_name = generate_random_string(10)

        with allure.step("Формирование тела запроса"):
            payload = {
                "login": login,
                "password": password,
                "firstName": first_name
            }

        with allure.step("Первая регистрация курьера"):
            response = requests.post(ApiPath.COURIER, data=payload)
            assert response.status_code == 201

        with allure.step("Повторная регистрация с теми же данными"):
            response_with_the_same_data = requests.post(ApiPath.COURIER, data=payload)

        with allure.step("Проверка кода и тела ответа"):
            assert response_with_the_same_data.status_code == 409
            assert response_with_the_same_data.json()["message"] == ApiErrors.CREATE_ERROR_WITH_THE_SAME_LOGIN

    def test_create_courier_without_login(self):
        with allure.step("Генерируем пароль и имя курьера"):
            password = generate_random_string(10)
            first_name = generate_random_string(10)

        with allure.step("Формирование тела запроса"):
            payload = {
                "password": password,
                "firstName": first_name
            }

        with allure.step("Отправляем запрос на регистрацию курьера"):
            response = requests.post(ApiPath.COURIER, data=payload)
        
        with allure.step("Проверка кода и тела ответа"):
            assert response.status_code == 400
            assert response.json()["message"] == ApiErrors.CREATE_ERROR

    def test_create_courier_without_password(self):
        with allure.step("Генерируем логин и имя курьера"):
            login = generate_random_string(10)
            first_name = generate_random_string(10)
        
        with allure.step("Формирование тела запроса"):
            payload = {
                "login": login,
                "firstName": first_name
            }

        with allure.step("Отправляем запрос на регистрацию курьера"):
            response = requests.post(ApiPath.COURIER, data=payload)
        
        with allure.step("Проверка кода и тела ответа"):
            assert response.status_code == 400
            assert response.json()["message"] == ApiErrors.CREATE_ERROR
