from selenium.webdriver.support.wait import WebDriverWait

from data.data_reset_password import DataCreateUser, DataResetPassword
from locator.locators import Locators
from pages.base_page import GeneralMethods
import requests

from urls import Urls


class PersonalCabinet(GeneralMethods):

    def creat_user_andlogin(self):
        response = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json = DataCreateUser.CREAT_USER)
        return response

    def enter_log_data(self):
        self.click_ver_ywo(self.driver, Locators.BUTTON_PERSONAL_ACCOUNT)
        self.insert_data_to_fild(Locators.ACCOUNT_EMAIL, DataCreateUser.LOGIN_USER['email'])
        self.insert_data_to_fild(Locators.ACCOUNT_PASSWORD, DataResetPassword.password)
        self.click_ver_ywo(self.driver, Locators.BUTTON_LOGIN)
        self.click_ver_ywo(self.driver, Locators.BUTTON_LOGIN)

    def log_in_new(self):
        self.creat_user_andlogin()
        self.enter_log_data()
        self.wait_element(self.driver, Locators.LOGO)
        self.wait_element(self.driver, Locators.BUTTON_MAKE_ORDER)
        self.click_ver_ywo(self.driver, Locators.BUTTON_PERSONAL_ACCOUNT)
        self.click_ver_ywo(self.driver, Locators.LINK_HISTORY_ORDER)

    def log_in_and_out(self):
        self.creat_user_andlogin()
        self.enter_log_data()
        self.wait_element(self.driver, Locators.BUTTON_MAKE_ORDER)
        self.click_ver_ywo(self.driver, Locators.BUTTON_PERSONAL_ACCOUNT)
        self.click_ver_ywo(self.driver, Locators.BUTTON_LOGOUT)
        self.wait_element(self.driver, Locators.BUTTON_LOGIN)



