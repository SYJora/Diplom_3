import allure

from data.data_reset_password import DataResetPassword
from helper import Helper
from locator.locators import Locators, LocatorBaseFunctionality
from pages.base_page import BasePage
from seletools.actions import drag_and_drop



class BasicFunctionality(BasePage):

    @allure.step('Нажимаем на ленту заказа возвращаем url страницы открываем Конструктор')
    def click_list_order_and_retern_onmain_page(self):
        self.find_click_element(Locators.BUTTON_LIST_ORDER)
        self.wait_element(LocatorBaseFunctionality.LIST_ORDER)
        self.find_click_element(Locators.BUTTON_DESIGNER)


    @allure.step('Нажимаем на ленту заказа возвращаем url страницы')
    def click_on_list_order(self):
        self.find_click_element(Locators.BUTTON_LIST_ORDER)
        self.wait_element(LocatorBaseFunctionality.LIST_ORDER)


    @allure.step('Ждем отображение ингридиента нажимаем на него')
    def click_ingredients_description(self):
        self.wait_element(LocatorBaseFunctionality.IMG_BUN)
        self.click_by_elemet_locator(LocatorBaseFunctionality.IMG_BUN)

    @allure.step('Нажимаем на крестик в карточки ингридиента')
    def click_cross_in_description_ingredients(self):
        self.click_ingredients_description()
        self.element_is_displayed(LocatorBaseFunctionality.BUTTON_CROSS)

    @allure.step('Переносим ингредиент в заказа')
    def move_ingredients_to_order(self):
        get = self.wait_and_search_element(LocatorBaseFunctionality.IMG_BUN)
        move_to = self.wait_and_search_element(LocatorBaseFunctionality.UP_BUN)
        drag_and_drop(self.driver, get, move_to)

    @allure.step('Делаем заказа авторизированным пользователем')
    def make_order_login_user(self):
        api = Helper()
        data = api.generet_data_for_api()
        api.creat_user_andlogin(data)
        self.find_click_element(Locators.BUTTON_PERSONAL_ACCOUNT)
        self.insert_data_to_fild(Locators.ACCOUNT_EMAIL, data['email'])
        self.insert_data_to_fild(Locators.ACCOUNT_PASSWORD, DataResetPassword.password)
        self.find_click_element(Locators.BUTTON_LOGIN)
        self.wait_element(Locators.LOGO)
        self.wait_element(Locators.BUTTON_MAKE_ORDER)
        self.find_click_element(Locators.BUTTON_PERSONAL_ACCOUNT)
        self.find_click_element(Locators.LINK_HISTORY_ORDER)
        self.find_click_element(Locators.LOGO)
        self.wait_element(Locators.BUTTON_MAKE_ORDER)
        self.move_ingredients_to_order()
        self.find_click_element(Locators.BUTTON_MAKE_ORDER)

