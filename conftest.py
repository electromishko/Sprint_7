import pytest
from helpers.user_registration import register_new_courier
from helpers.delete_user import delete_user


class Courier:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.user_id = 0


@pytest.fixture
def create_courier():
    # Регистрируем курьера
    courier_data = register_new_courier()
    courier = Courier(courier_data["login"], courier_data["password"])
    
    yield courier  # передаем тесту
    
    # Удаляем после теста
    if courier.user_id:
        delete_user(courier.user_id)


@pytest.fixture
def random_courier_data():
    from helpers.user_registration import generate_random_courier_data
    return generate_random_courier_data()
