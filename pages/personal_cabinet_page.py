import string
import random

import allure

from data.data_reset_password import DataCreateUser, DataResetPassword
from locator.locators import Locators
from pages.base_page import GeneralMethods
import requests

from urls import Urls


class PersonalCabinet(GeneralMethods):
    @allure.step('Создать пользователя и вернуть респонс ответ')
    def creat_user_andlogin(self,data):
        response = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json = data)
        return response

    @allure.step('Сгенерировать данные для логирования пользователя через апи')
    def generet_data_for_api(self):
        def generate_random_word(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(length))
        data = {
            "email": f"{generate_random_word(7)}@mail.ru",
            "password": "121345",
            "name": 'test'

        }
        return data

    @allure.step('Войти в акаунт')
    def enter_log_data(self, data):
        self.click_ver_two(self.driver, Locators.BUTTON_PERSONAL_ACCOUNT)
        self.insert_data_to_fild(Locators.ACCOUNT_EMAIL, data['email'])
        self.insert_data_to_fild(Locators.ACCOUNT_PASSWORD, DataResetPassword.password)
        self.click_ver_two(self.driver, Locators.BUTTON_LOGIN)

    @allure.step('Новый пользователь входит в систему')
    def log_in_new(self):
        data = self.generet_data_for_api()
        self.creat_user_andlogin(data)
        self.enter_log_data(data)
        self.wait_element(self.driver, Locators.LOGO)
        self.wait_element(self.driver, Locators.BUTTON_MAKE_ORDER)
        self.click_ver_two(self.driver, Locators.BUTTON_PERSONAL_ACCOUNT)
        self.click_ver_two(self.driver, Locators.LINK_HISTORY_ORDER)

    @allure.step('Новый пользователь входит и выходит из системы')
    def log_in_and_out(self):
        data = self.generet_data_for_api()
        self.creat_user_andlogin(data)
        self.enter_log_data(data)
        self.wait_element(self.driver, Locators.BUTTON_MAKE_ORDER)
        self.click_ver_two(self.driver, Locators.BUTTON_PERSONAL_ACCOUNT)
        self.click_ver_two(self.driver, Locators.BUTTON_LOGOUT)
        self.wait_element(self.driver, Locators.BUTTON_LOGIN)





