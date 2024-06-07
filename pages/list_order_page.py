

import allure

from selenium.webdriver.common.by import By
from seletools.actions import drag_and_drop

from data.data_reset_password import DataCreateUser, DataResetPassword
from helper import Helper
from locator.locators import LocatorBaseFunctionality, Locators, LocatorListOrder
from pages.base_page import BasePage


class ListOrder(BasePage):

    @allure.step('Нажатие на кнопку Лента заказа')
    def select_list_order(self):
        self.find_click_element(Locators.LOGO)
        self.click_by_elemet_locator(Locators.BUTTON_LIST_ORDER)

    @allure.step('Нажатие на кнопку персональный аккаунт')
    def press_personal_account(self):
        self.wait_element(Locators.BUTTON_MAKE_ORDER)
        self.find_click_element(Locators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Получить номер заказа из Историй заказов')
    def get_order_from_history(self, order):
        self.wait_element(Locators.LINK_HISTORY_ORDER)
        self.find_click_element(Locators.LINK_HISTORY_ORDER)
        self.wait_and_search_element((By.XPATH, f"//p[contains(text(), '#0{order}')]"))
        num_order = self.get_text_from_element((By.XPATH, f"//p[contains(text(), '#0{order}')]"))
        return num_order

    @allure.step('Логирование в персональный кабинет')
    def log_in_personal_cabinet(self, data):
        self.insert_data_to_fild(Locators.ACCOUNT_EMAIL, data)
        self.insert_data_to_fild(Locators.ACCOUNT_PASSWORD, DataCreateUser.CREAT_USER['password'])
        self.click_by_elemet_locator(Locators.BUTTON_LOGIN)

    @allure.step('Нажатие кнопки Личный кабинет')
    def enter_to_personal_cabinet(self, data):
        self.find_click_element(Locators.BUTTON_PERSONAL_ACCOUNT)
        self.log_in_personal_cabinet(data)

    @allure.step('Получение номера заказа из Ленты заказов')
    def list_order_get_number_order(self, order):
        self.wait_and_search_element((By.XPATH, f"//p[contains(text(), '{order}')]"))
        return self.element_is_displayed((By.XPATH, f"//p[contains(text(), '{order}')]"))

    @allure.step('Нажатие на первый заказ из Ленты заказов')
    def select_first_order_in_list(self):
        self.select_list_order()
        self.find_click_element(LocatorListOrder.FIRST_ORDER)

    @allure.step('Войти в акаунт')
    def enter_log_data(self, data):
        self.find_click_element(Locators.BUTTON_PERSONAL_ACCOUNT)
        self.insert_data_to_fild(Locators.ACCOUNT_EMAIL, data['email'])
        self.insert_data_to_fild(Locators.ACCOUNT_PASSWORD, DataResetPassword.password)
        self.find_click_element(Locators.BUTTON_LOGIN)

    @allure.step('Переносим ингредиент в заказа')
    def move_ingredients_to_order(self):
        get = self.wait_and_search_element(LocatorBaseFunctionality.IMG_BUN)
        move_to = self.wait_and_search_element(LocatorBaseFunctionality.UP_BUN)
        drag_and_drop(self.driver, get, move_to)

    @allure.step('Проверка заказ в истроий и ленте заказа')
    def check_order_in_history_and_list_order(self):
        api = Helper()
        respons = api.make_oder_api()
        num = respons.json()['order']['number']
        self.enter_to_personal_cabinet(respons.json()['order']['owner']['email'])
        self.press_personal_account()
        history_order = self.get_order_from_history(num)
        self.select_list_order()
        return self.list_order_get_number_order(history_order)

    @allure.step('Получить значение из выполненын всего заказов')
    def get_count_of_common(self):
        self.select_list_order()
        befor = self.get_text_from_element(LocatorListOrder.COUNT_DEFOULT)
        return befor

    @allure.step('Создать заказ и вернуть значение счетчика выполненых заказов всего')
    def make_order_and_returncurrent_count(self):
        api = Helper()
        api.make_oder_api()
        return self.get_text_from_element(LocatorListOrder.COUNT_DEFOULT)

    @allure.step('Получить значение из выполненын заказов за сегодня')
    def get_count_make_burger_a_day(self):
        self.select_list_order()
        befor = self.get_text_from_element(LocatorListOrder.DONE_COUNT)
        return befor

    @allure.step('Создать заказ и вернуть значение счетчика выполненого заказов за сегодня')
    def get_new_count_make_burger_a_day(self):
        api = Helper()
        api.make_oder_api()
        return self.get_text_from_element(LocatorListOrder.DONE_COUNT)

    @allure.step('Создание пользователя и добавление заказа')
    def creat_user_add_ingredirnts(self):
        user = Helper()
        data = user.generet_data_for_api()
        user.creat_user_andlogin(data)
        self.enter_log_data(data)
        self.move_ingredients_to_order()
        self.find_click_element(Locators.BUTTON_MAKE_ORDER)
        self.click_escepe()
        self.wait_until_not_visibl(LocatorListOrder.PROGRES_BAR)
        self.find_click_element(Locators.BUTTON_LIST_ORDER)
        self.wait_element(LocatorListOrder.FIRST_ORDER)
        return self.get_text_from_element(LocatorListOrder.STATYS_ORDER)











