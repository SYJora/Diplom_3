import allure

from locator.locators import LocatorBaseFunctionality
from pages.basic_functionality import BasicFunctionality
from urls import Urls


class TestBasicFunctionality:

    @allure.title('Проверка кнопки Конструктор')
    @allure.description('После нажатия на кнопку конструктор выполняется переход на главную страницу.')
    def test_click_on_constructor(self, driver):
        base = BasicFunctionality(driver)
        base.click_list_order_and_retern_onmain_page()
        assert driver.current_url == Urls.BASE_URL

    @allure.title('Проверка кнопки Лента заказов.')
    @allure.description('Нажатие на кнопку Лента заказов выполняется переход на страницу заказов.')
    def test_click_on_list_order(self, driver):
        base = BasicFunctionality(driver)
        base.click_on_list_order()
        assert driver.current_url == Urls.LIST_ORDER

    @allure.title('Описание Ингридиента.')
    @allure.description('При нажатий на ингридиента открывается карточка описания ингридиента.')
    def test_open_description_ingredients(self, driver):
        base = BasicFunctionality(driver)
        base.click_ingredients_description()
        assert base.element_is_displayed(LocatorBaseFunctionality.DETAILS_ORDER) == True

    @allure.title('Нажатие на крестик')
    @allure.description('Проверка закрытия карточки ингридиента нажатием на крестик')
    def test_description_ingredients_close_click_by_cross(self, driver):
        base = BasicFunctionality(driver)
        base.click_cross_in_description_ingredients()
        res = base.element_is_displayed(LocatorBaseFunctionality.DETAILS_ORDER)
        assert res == True

    @allure.title('Добавление ингредиента в заказ')
    @allure.description('Добавление булок в заказ')
    def test_adding_ingredient_to_order_counter_and_ingredient_incremented(self, driver):
        base = BasicFunctionality(driver)
        base.move_ingredients_to_order()
        assert base.element_is_displayed(LocatorBaseFunctionality.TWO_BUN_COUNTER) == True

    @allure.title('Оформление заказа авторизированным пользователем')
    @allure.description('Пользователь создан через API им делаем заказ')
    def test_log_in_user_place_an_order(self, driver):
        base = BasicFunctionality(driver)
        base.make_order_login_user()
        base.wait_text_in_element(LocatorBaseFunctionality.TEXT_ORDER_START_COOK, 'Ваш заказ начали готовить')
        assert base.element_is_displayed(LocatorBaseFunctionality.TEXT_ORDER_START_COOK) == True
