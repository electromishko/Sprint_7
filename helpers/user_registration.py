import allure
import requests
from data import ApiPath
from helpers.generators import generate_random_string


def register_new_courier():
    """Регистрирует нового курьера и возвращает данные"""
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    with allure.step("Отправляем запрос на регистрацию курьера"):
        response = requests.post(ApiPath.COURIER, data=payload)

    if response.status_code == 201:
        return {
            "login": login,
            "password": password, 
            "first_name": first_name
        }
    return None


def generate_random_courier_data():
    """Генерирует данные для курьера (без регистрации)"""
    return {
        "login": generate_random_string(9),
        "password": generate_random_string(8),
        "first_name": generate_random_string(8)
    }
