import random
import string
import requests


class Helpers:
    def generate_random_string_fixture(self):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(10))
        return random_string

    def register_new_courier_and_return_login_password(self):
        login_pass = []

        login = self.generate_random_string_fixture()
        password = self.generate_random_string_fixture()
        first_name = self.generate_random_string_fixture()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass
