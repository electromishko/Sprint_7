import allure
import requests
from data import ApiPath
from helpers.validation import validate_json


class TestStationsSearch:
    def test_successful_stations_search(self):
        with allure.step("Ищем станции метро по запросу 'Площадь'"):
            params = {"s": "Площадь"}
            response = requests.get(ApiPath.STATIONS_SEARCH, params=params)

        with allure.step("Проверка кода и тела ответа"):

            assert response.status_code == 200
            stations = response.json()
            assert isinstance(stations, list)
            assert len(stations) == 3

            # Проверка структуры ответа
            required_fields = ["number", "name", "color"]
            for station in stations:
                validate_json(station, required_fields)

            with allure.step("Проверка содержания названий станций"):
                station_names = [station["name"] for station in stations]
                allure.attach(f"Found stations: {station_names}", "Found Stations", allure.attachment_type.TEXT)
                for name in station_names:
                    assert "Площадь" in name
