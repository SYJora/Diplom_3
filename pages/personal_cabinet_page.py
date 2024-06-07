

import allure

from data.data_reset_password import DataResetPassword
from helper import Helper
from locator.locators import Locators
from pages.base_page import BasePage




class PersonalCabinet(BasePage):

    @allure.step('Войти в акаунт')
    def enter_log_data(self, data):
        self.find_click_element(Locators.BUTTON_PERSONAL_ACCOUNT)
        self.insert_data_to_fild(Locators.ACCOUNT_EMAIL, data['email'])
        self.insert_data_to_fild(Locators.ACCOUNT_PASSWORD, DataResetPassword.password)
        self.find_click_element(Locators.BUTTON_LOGIN)

    @allure.step('Новый пользователь входит в систему')
    def log_in_new(self):
        api = Helper()
        data = api.generet_data_for_api()
        api.creat_user_andlogin(data)
        self.enter_log_data(data)
        self.wait_element(Locators.LOGO)
        self.wait_element(Locators.BUTTON_MAKE_ORDER)
        self.find_click_element(Locators.BUTTON_PERSONAL_ACCOUNT)
        self.find_click_element(Locators.LINK_HISTORY_ORDER)

    @allure.step('Новый пользователь входит и выходит из системы')
    def log_in_and_out(self):
        api = Helper()
        data = api.generet_data_for_api()
        api.creat_user_andlogin(data)
        self.enter_log_data(data)
        self.wait_element(Locators.BUTTON_MAKE_ORDER)
        self.find_click_element(Locators.BUTTON_PERSONAL_ACCOUNT)
        self.find_click_element(Locators.BUTTON_LOGOUT)
        self.wait_element(Locators.BUTTON_LOGIN)





