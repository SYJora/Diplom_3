from pages.base_page import GeneralMethods



class DataResetPassword:
    email = 'teretey@gmail.com'
    password = 12134

class DataCreateUser:

    login = GeneralMethods.generate_random_word(5)
    name = GeneralMethods.generate_random_word(5)

    CREAT_USER = {
        "email": f"{login}@mail.ru",
        "password": "12134",
        "name": name
    }

    LOGIN_USER = {
        "email": f"{login}@mail.ru",
        "password": "12134"
    }