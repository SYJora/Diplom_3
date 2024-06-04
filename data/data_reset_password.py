import string
import random

class DataResetPassword:
    email = 'teretey@gmail.com'
    password = 121345

class DataCreateUser:

    def generate_random_word(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))


    CREAT_USER = {
        "email": f"{generate_random_word(7)}@mail.ru",
        "password": "121345",
        "name": 'test'


    }

    LOGIN_USER = {
        "email": f"{generate_random_word(7)}@mail.ru",
        "password": "12134"
    }


