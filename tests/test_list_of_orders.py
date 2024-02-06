import requests
import allure
from data import EndpointsUrl


class TestListOrder:
    @allure.feature("Тест на возврат списка заказов")
    @allure.title('Проверка того что в тело ответа возвращается список заказов')
    def test_list_order(self):
        request_url = (EndpointsUrl.ORDER)
        with allure.step("Шаг 1: Отправка GET-запроса на получение списка заказов"):
            response = requests.get(request_url)
        with allure.step("Шаг 2: Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Шаг 3: Проверка что в ответе содержится список заказов"):
            assert "orders" in response.json() and type(response.json()["orders"]) is list
