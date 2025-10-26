class Data:
    URL = 'https://qa-scooter.praktikum-services.ru/'

class ApiPath:
    BASE = Data.URL + "api/v1"
    COURIER = f"{BASE}/courier"
    LOGIN = f"{BASE}/courier/login"
    ORDER = f"{BASE}/orders"
    ORDER_ACCEPT = f"{BASE}/orders/accept"
    TRACK = f"{BASE}/orders/track"
    PING = f"{BASE}/ping"
    STATIONS_SEARCH = f"{BASE}/stations/search"


class ApiErrors:
    CREATE_ERROR = "Недостаточно данных для создания учетной записи"
    CREATE_ERROR_WITH_THE_SAME_LOGIN = "Этот логин уже используется. Попробуйте другой."
    LOGIN_ERROR = "Учетная запись не найдена"
    LOGIN_ERROR_WITHOUT_FILEDS = "Недостаточно данных для входа"
    DELETE_WITHOUT_ID = "Not Found."
    DELETE_ERROR_WITH_INCORRECT_ID = "Курьера с таким id нет."
    ACCEPT_ORDER_WITHOUT_IDS = "Недостаточно данных для поиска"
    ACCEPT_ORDER_WITH_INCORRECT_ID_ORDER = "Заказа с таким id не существует"
    ACCEPT_ORDER_WITH_INCORRECT_ID_COURIER = "Курьера с таким id не существует"
    PING_OK = 'pong;'
