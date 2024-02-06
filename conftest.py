import requests
import random
import string
import pytest

@pytest.fixture(scope="function")
def generate_random_string_fixture():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string

@pytest.fixture(scope="function")
def register_new_courier_and_return_login_password(generate_random_string_fixture):
    login_pass = []

    login = generate_random_string_fixture
    password = generate_random_string_fixture
    first_name = generate_random_string_fixture

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