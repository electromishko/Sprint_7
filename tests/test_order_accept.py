import allure
import requests
from data import ApiPath, ApiErrors


class TestOrderAccept:
    def test_successful_accept_order(self, create_courier):
        with allure.step("Получаем список заказов"):
            response_order = requests.get(ApiPath.ORDER)
            assert response_order.status_code == 200
        
        with allure.step("Сохраняем ID заказа"):
            order_id = response_order.json()["orders"][0]["id"]
        
        with allure.step("Логиним курьера"):
            payload_courier = {
                "login": create_courier.login,
                "password": create_courier.password
            }
            response_login = requests.post(ApiPath.LOGIN, data=payload_courier)
            create_courier.user_id = response_login.json()["id"]
            assert response_login.status_code == 200
        
        with allure.step("Принимаем заказ"):
            params = {"courierId": create_courier.user_id}
            response_accept_order = requests.put(f"{ApiPath.ORDER_ACCEPT}/{order_id}", params=params)
        
        with allure.step("Проверка кода и тела ответа"):
            assert response_accept_order.status_code == 200
            assert response_accept_order.json()["ok"] == True

    def test_unsuccessful_accept_order_without_id_courier(self):
        with allure.step("Получаем список заказов"):
            response_order = requests.get(ApiPath.ORDER)
            assert response_order.status_code == 200
        
        with allure.step("Сохраняем ID заказа"):
            order_id = response_order.json()["orders"][0]["id"]
        
        with allure.step("Пытаемся принять заказ без ID курьера"):
            params = {"courierId": ""}
            response_accept_order = requests.put(f"{ApiPath.ORDER_ACCEPT}/{order_id}", params=params)
        
        with allure.step("Проверка кода и тела ответа"):
            assert response_accept_order.status_code == 400
            assert response_accept_order.json()["message"] == ApiErrors.ACCEPT_ORDER_WITHOUT_IDS

    def test_unsuccessful_accept_order_without_id_order(self, create_courier):
        with allure.step("Логиним курьера"):
            payload_courier = {
                "login": create_courier.login,
                "password": create_courier.password
            }
            response_login = requests.post(ApiPath.LOGIN, data=payload_courier)
            create_courier.user_id = response_login.json()["id"]
            assert response_login.status_code == 200
        
        with allure.step("Запрос принять заказ без ID заказа в URL"):       
            allure.attach(f"URL: {ApiPath.ORDER_ACCEPT}", "Request URL", allure.attachment_type.TEXT)
            response_accept_order = requests.put(f'{ApiPath.ORDER_ACCEPT}/courierId={create_courier.user_id}')
    
        with allure.step("Проверка кода и тела ответа"):
            allure.attach(f"Response Status: {response_accept_order.status_code}", "Response Status", allure.attachment_type.TEXT)
            allure.attach(f"Response Body: {response_accept_order.text}", "Response Body", allure.attachment_type.TEXT)
            
            assert response_accept_order.status_code == 400
            assert response_accept_order.json()["message"] == ApiErrors.ACCEPT_ORDER_WITHOUT_IDS

    def test_unsuccessful_accept_order_with_incorrect_id_courier(self):
        with allure.step("Получаем список заказов"):
            response_order = requests.get(ApiPath.ORDER)
            assert response_order.status_code == 200
        
        with allure.step("Сохраняем ID заказа"):
            order_id = response_order.json()["orders"][0]["id"]
        
        with allure.step("Пытаемся принять заказ с неверным ID курьера"):
            params = {"courierId": "111"}
            response_accept_order = requests.put(f"{ApiPath.ORDER_ACCEPT}/{order_id}", params=params)
        
        with allure.step("Проверка кода и тела ответа"):
            assert response_accept_order.status_code == 404
            assert response_accept_order.json()["message"] == ApiErrors.ACCEPT_ORDER_WITH_INCORRECT_ID_COURIER

    def test_unsuccessful_accept_order_with_incorrect_id_order(self, create_courier):
        with allure.step("Логиним курьера"):
            payload_courier = {
                "login": create_courier.login,
                "password": create_courier.password
            }
            response_login = requests.post(ApiPath.LOGIN, data=payload_courier)
            create_courier.user_id = response_login.json()["id"]
            assert response_login.status_code == 200
        
        with allure.step("Пытаемся принять заказ с неверным ID заказа"):
            params = {"courierId": create_courier.user_id}
            response_accept_order = requests.put(f"{ApiPath.ORDER_ACCEPT}/111", params=params)
        
        with allure.step("Проверка кода и тела ответа"):
            assert response_accept_order.status_code == 404
            assert response_accept_order.json()["message"] == ApiErrors.ACCEPT_ORDER_WITH_INCORRECT_ID_ORDER
