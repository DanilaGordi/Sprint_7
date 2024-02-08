import allure
import requests
from data import EndpointsUrl
from helpers import Helpers


@allure.feature('Создание курьера')
class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера, и что вернулись ожидаемые код и текст ответа об успешном создании')
    def test_create_courier_success(self):
        helper = Helpers()

        login = helper.generate_random_string_fixture()
        password = helper.generate_random_string_fixture()
        first_name = helper.generate_random_string_fixture()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(EndpointsUrl.CREATE_COURIER, data=payload)
        success_message = '{"ok":true}'
        assert 201 == response.status_code and success_message in response.text

    @allure.title('Создание курьера повторно')
    def test_create_courier_fail(self):
        helper = Helpers()
        login, password, first_name = helper.register_new_courier_and_return_login_password()
        response = requests.post(EndpointsUrl.CREATE_COURIER,
                                 json={'login': login, 'password': password, 'first_name': first_name})
        error_message = "Этот логин уже используется. Попробуйте другой."
        assert 409 == response.status_code and error_message in response.text

    @allure.title('Создание курьера без имени')
    def test_without_first_name(self):
        helper = Helpers()
        login = helper.generate_random_string_fixture()
        password = helper.generate_random_string_fixture()
        first_name = helper.generate_random_string_fixture()

        payload = {
            "login": login,
            "password": password,
        }

        response = requests.post(EndpointsUrl.CREATE_COURIER, data=payload)
        assert response.status_code == 201

    @allure.title('Создание курьера без логина')
    def test_without_login(self):
        helper = Helpers()

        login = helper.generate_random_string_fixture()
        password = helper.generate_random_string_fixture()
        first_name = helper.generate_random_string_fixture()

        payload = {
            "password": password,
            "firstName": first_name
        }

        response = requests.post(EndpointsUrl.CREATE_COURIER, data=payload)
        error_message = 'Недостаточно данных для создания учетной записи'
        assert 400 == response.status_code and error_message in response.text

    @allure.title('Создание курьера без пароля')
    def test_without_password(self):
        helper = Helpers()
        login = helper.generate_random_string_fixture()
        password = helper.generate_random_string_fixture()
        first_name = helper.generate_random_string_fixture()

        payload = {
            "login": login,
            "firstName": first_name
        }

        response = requests.post(EndpointsUrl.CREATE_COURIER, data=payload)
        error_message = 'Недостаточно данных для создания учетной записи'
        assert 400 == response.status_code and error_message in response.text


