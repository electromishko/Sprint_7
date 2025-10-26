import allure
import requests
from data import ApiPath, ApiErrors


class TestCourierDelete:
    def test_successful_delete_courier(self, create_courier):
        with allure.step("Формирование тела запроса для логина"):
            payload = {
                "login": create_courier.login,
                "password": create_courier.password
            }

        with allure.step("Логиним курьера для получения ID"):
            response = requests.post(ApiPath.LOGIN, data=payload)
            user_id = response.json()["id"]
        
        with allure.step("Удаляем курьера"):
            delete_url = f"{ApiPath.COURIER}/{user_id}"
            response_delete = requests.delete(delete_url)
        
        with allure.step("Проверка кода и тела ответа"):
            allure.attach(f"Request URL: DELETE {delete_url}", "Request Details", allure.attachment_type.TEXT)
            allure.attach(f"Response Status: {response_delete.status_code}", "Response Status", allure.attachment_type.TEXT)
            allure.attach(f"Response Body: {response_delete.text}", "Response Body", allure.attachment_type.TEXT)
            
            assert response_delete.status_code == 200
            assert response_delete.json()["ok"] == True

    def test_unsuccessful_delete_courier_without_id(self):
            with allure.step("запрос удаления курьера без указания ID"):
                response = requests.delete(f"{ApiPath.COURIER}/")
            with allure.step("проверка кода и тела ответа"):
                assert response.status_code == 404
                assert response.json()["message"] == ApiErrors.DELETE_WITHOUT_ID

    def test_unsuccessful_delete_courier_with_incorrect_id(self):
        with allure.step("Пытаемся удалить курьера с неверным ID"):
            delete_url = f"{ApiPath.COURIER}/111"
            response = requests.delete(delete_url)
        
        with allure.step("Детальный вывод запроса и ответа"):
            allure.attach(f"Request URL: DELETE {delete_url}", "Request Details", allure.attachment_type.TEXT)
            allure.attach(f"Response Status: {response.status_code}", "Response Status", allure.attachment_type.TEXT)
            allure.attach(f"Response Body: {response.text}", "Response Body", allure.attachment_type.TEXT)
        
        with allure.step("Проверка кода и тела ответа"):
            assert response.status_code == 404
            assert response.json()["message"] == ApiErrors.DELETE_ERROR_WITH_INCORRECT_ID
