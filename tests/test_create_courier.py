import allure
from data import EndpointsUrl
from conftest import *


@allure.feature('Создание курьера')
class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера, и что вернулись ожидаемые код и текст ответа об успешном создании')
    def test_create_courier_success(self, generate_random_string_fixture):

        login = generate_random_string_fixture
        password = generate_random_string_fixture
        first_name = generate_random_string_fixture

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(EndpointsUrl.CREATE_COURIER, data=payload)
        assert response.status_code == 201 and response.json() == {"ok": True}

    @allure.title('Создание курьера повторно')
    def test_create_courier_fail(self, register_new_courier_and_return_login_password, generate_random_string_fixture):
        login, password, first_name = register_new_courier_and_return_login_password
        response = requests.post(EndpointsUrl.CREATE_COURIER,
                                 json={'login': login, 'password': password, 'first_name': first_name})
        assert response.status_code == 409

    @allure.title('Создание курьера без имени')
    def test_without_first_name(self, generate_random_string_fixture):
        login = generate_random_string_fixture
        password = generate_random_string_fixture
        first_name = generate_random_string_fixture

        payload = {
            "login": login,
            "password": password,
        }

        response = requests.post(EndpointsUrl.CREATE_COURIER, data=payload)
        assert response.status_code == 201

    @allure.title('Создание курьера без логина')
    def test_without_login(self, generate_random_string_fixture):

        login = generate_random_string_fixture
        password = generate_random_string_fixture
        first_name = generate_random_string_fixture

        payload = {
            "password": password,
            "firstName": first_name
        }

        response = requests.post(EndpointsUrl.CREATE_COURIER, data=payload)
        assert response.status_code == 400

    @allure.title('Создание курьера без пароля')
    def test_without_password(self, generate_random_string_fixture):
        login = generate_random_string_fixture
        password = generate_random_string_fixture
        first_name = generate_random_string_fixture

        payload = {
            "login": login,
            "firstName": first_name
        }

        response = requests.post(EndpointsUrl.CREATE_COURIER, data=payload)
        assert response.status_code == 400


