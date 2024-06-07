
from pages.base_page import BasePage


class DataResetPassword:
    email = 'teretey@gmail.com'
    password = 121345

class DataCreateUser:


    CREAT_USER = {
        "email": f"{BasePage.generate_random_word(7)}@mail.ru",
        "password": "121345",
        "name": 'test'


    }



