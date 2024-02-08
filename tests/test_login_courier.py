import allure
from data import EndpointsUrl
from helpers import Helpers
import requests


@allure.feature('Логин курьера')
class TestLoginCourier:


    @allure.title('Успешная авторизация курьера')
    def test_login_courier_success(self):
        helper = Helpers()
        login, password, first_name = helper.register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(EndpointsUrl.LOGIN, data=payload)

        assert response.status_code == 200

    @allure.title('Авторизация курьера с некорректным паролем')
    def test_login_with_incorrect_password(self):
        helper = Helpers()
        login, password, first_name = helper.register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": 'wrong'
        }
        response = requests.post(EndpointsUrl.LOGIN, data=payload)
        error_message = 'Учетная запись не найдена'
        assert 404 == response.status_code and error_message in response.text

    @allure.title('Авторизация несуществующего пользователя')
    def test_login_non_existent_user(self):
        payload = {
            "login": 'nobody',
            "password": '10101'
        }
        response = requests.post(EndpointsUrl.LOGIN, data=payload)
        error_message = 'Учетная запись не найдена'
        assert 404 == response.status_code and error_message in response.text

    @allure.title('Авторизация пользователя без одного поля')
    def test_login_courier_missing_one_attribute(self):
        payload = {
            "password": '12345'
        }
        response = requests.post(EndpointsUrl.LOGIN, data=payload)
        error_message = 'Недостаточно данных для входа'
        assert 400 == response.status_code and error_message in response.text

    @allure.title('Возврат id при успешной авторизации')
    def test_successful_request_return_id(self):
        helper = Helpers()
        login, password, first_name = helper.register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(EndpointsUrl.LOGIN, data=payload)
        assert "id" in response.text
