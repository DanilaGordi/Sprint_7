import allure
from conftest import *
from data import EndpointsUrl


@allure.feature('Логин курьера')
class TestLoginCourier:


    @allure.title('Успешная авторизация курьера')
    def test_login_courier_success(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(EndpointsUrl.LOGIN, data=payload)

        assert response.status_code == 200

    @allure.title('Авторизация курьера с некорректным паролем')
    def test_login_with_incorrect_password(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password

        payload = {
            "login": login,
            "password": 'wrong'
        }
        response = requests.post(EndpointsUrl.LOGIN, data=payload)

        assert response.status_code == 404

    @allure.title('Авторизация несуществующего пользователя')
    def test_login_non_existent_user(self):
        payload = {
            "login": 'nobody',
            "password": '10101'
        }
        response = requests.post(EndpointsUrl.LOGIN, data=payload)

        assert response.status_code == 404

    @allure.title('Авторизация пользователя без одного поля')
    def test_login_courier_missing_one_attribute(self):
        payload = {
            "password": '12345'
        }
        response = requests.post(EndpointsUrl.LOGIN, data=payload)

        assert response.status_code == 400

    @allure.title('Возврат id при успешной авторизации')
    def test_successful_request_return_id(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(EndpointsUrl.LOGIN, data=payload)
        assert "id" in response.text
