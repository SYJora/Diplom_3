import requests
from selenium.webdriver.common.by import By

from data.data_reset_password import DataCreateUser
from locator.locators import LocatorBaseFunctionality, Locators
from pages.base_page import GeneralMethods
from pages.personal_cabinet_page import PersonalCabinet
from urls import Urls


class ListOrder(GeneralMethods):

    def select_list_order(self):
        self.click_ver_two(self.driver, Locators.LOGO)
        self.click_by_elemet_locator(LocatorBaseFunctionality.BUTTON_LIST_ORDER)

    def press_personal_account(self):
        self.wait_element(self.driver, Locators.BUTTON_MAKE_ORDER)
        self.click_ver_two(self.driver, Locators.BUTTON_PERSONAL_ACCOUNT)

    def get_ingredients(self):
        respons = requests.get(Urls.BASE_URL + Urls.LIST_INGR)
        ingr = []
        for i in range(3):
            ingr.append(respons.json()['data'][i]['_id'])
        return ingr

    def make_oder_api(self):
        user = PersonalCabinet(self.driver)
        response = user.creat_user_andlogin()
        respons = requests.post(Urls.BASE_URL + Urls.ORDER,
                                headers={"Authorization": response.json()['accessToken']},
                                json={"ingredients": self.get_ingredients()})
        return respons

    def get_order_from_history(self, order):
        self.wait_element(self.driver, Locators.LINK_HISTORY_ORDER)
        self.click_ver_two(self.driver, Locators.LINK_HISTORY_ORDER)
        num_order = self.get_text_from_element((By.XPATH, f"//p[contains(text(), '#0{order}')]"))
        return num_order

    def log_in_personal_cabinet(self):
        self.insert_data_to_fild(Locators.ACCOUNT_EMAIL, DataCreateUser.CREAT_USER['email'])
        self.insert_data_to_fild(Locators.ACCOUNT_PASSWORD, DataCreateUser.CREAT_USER['password'])
        self.click_by_elemet_locator(Locators.BUTTON_LOGIN)


    def enter_to_personal_cabinet(self):
        self.click_ver_two(self.driver, Locators.BUTTON_PERSONAL_ACCOUNT)
        self.log_in_personal_cabinet()

    def list_order_get_number_order(self, order):
        return self.element_is_displayed((By.XPATH, f"//p[contains(text(), '#0{order}')]"))







