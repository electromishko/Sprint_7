import allure
import requests
from helpers.validation import validate_order_response
from helpers.generators import generate_order_payload
from data import ApiPath


class TestOrderGet:
    def test_order_get_by_id_successful(self):
        with allure.step("Генерация данных для заказа"):
            payload = generate_order_payload()
            
            response_create = requests.post(ApiPath.ORDER, data=payload)
            assert response_create.status_code == 201
            order_track = response_create.json()["track"]
        
        with allure.step("Получаем заказ по трек-номеру"):
            params = {"t": order_track}
            response_get = requests.get(ApiPath.TRACK, params=params)
            
            assert response_get.status_code == 200
            validate_order_response(response_get.json())
    
    def test_get_nonexistent_order(self):
        with allure.step("Пытаемся получить несуществующий заказ"):
            params = {"t": 999999}
            response = requests.get(ApiPath.TRACK, params=params)
            
            assert response.status_code == 404
    
    def test_get_order_without_track_number(self):
        with allure.step("Пытаемся получить заказ без номера"):
            response = requests.get(ApiPath.TRACK)
            
            assert response.status_code == 400
