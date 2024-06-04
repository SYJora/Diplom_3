
from pages.base_page import GeneralMethods



class DataResetPassword:
    email = 'teretey@gmail.com'
    password = 121345

class DataCreateUser:

    login = GeneralMethods.generate_random_word(7)


    CREAT_USER = {
        "email": f"{GeneralMethods.generate_random_word(7)}@mail.ru",
        "password": "121345",
        "name": 'test'


    }

    LOGIN_USER = {
        "email": f"{login}@mail.ru",
        "password": "12134"
    }


