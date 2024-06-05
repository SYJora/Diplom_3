import allure

from locator.locators import Locators, LocatorBaseFunctionality
from pages.base_page import GeneralMethods
from seletools.actions import drag_and_drop

from pages.personal_cabinet_page import PersonalCabinet


class BasicFunctionality(GeneralMethods):

    @allure.step('Нажимаем на ленту заказа возвращаем url страницы открываем Конструктор')
    def click_list_order_and_retern_onmain_page(self):
        self.click_ver_two(self.driver, Locators.BUTTON_LIST_ORDER)
        self.wait_element(self.driver, LocatorBaseFunctionality.LIST_ORDER)
        urls = self.driver.current_url
        self.click_ver_two(self.driver, Locators.BUTTON_DESIGNER)
        return urls

    @allure.step('Нажимаем на ленту заказа возвращаем url страницы')
    def click_on_list_order(self):
        self.click_ver_two(self.driver, Locators.BUTTON_LIST_ORDER)
        self.wait_element(self.driver, LocatorBaseFunctionality.LIST_ORDER)
        urlds = self.driver.current_url
        return urlds

    @allure.step('Ждем отображение ингридиента нажимаем на него')
    def click_ingredients_description(self):
        self.wait_element(self.driver, LocatorBaseFunctionality.IMG_BUN)
        self.click_by_elemet_locator(LocatorBaseFunctionality.IMG_BUN)

    @allure.step('Нажимаем на крестик в карточки ингридиента')
    def click_cross_in_description_ingredients(self):
        self.click_ingredients_description()
        self.element_is_displayed(LocatorBaseFunctionality.BUTTON_CROSS)

    @allure.step('Переносим ингредиент в заказа')
    def move_ingredients_to_order(self):
        get = self.wait_and_search_element(self.driver, LocatorBaseFunctionality.IMG_BUN)
        move_to = self.wait_and_search_element(self.driver, LocatorBaseFunctionality.UP_BUN)
        drag_and_drop(self.driver, get, move_to)

    @allure.step('Делаем заказа авторизированным пользователем')
    def make_order_login_user(self):
        login = PersonalCabinet(self.driver)
        login.log_in_new()
        login.click_ver_two(self.driver, Locators.LOGO)
        self.wait_element(self.driver, Locators.BUTTON_MAKE_ORDER)
        self.move_ingredients_to_order()
        self.click_ver_two(self.driver, Locators.BUTTON_MAKE_ORDER)

