import allure

from pages.basic_functionality import BasicFunctionality
from urls import Urls


class TestBasicFunctionality:

    @allure.title('Проверка кнопки Конструктор')
    @allure.description('После нажатия на кнопку конструктор выполняется переход на главную страницу.')
    def test_click_on_constructor(self, driver):
        base = BasicFunctionality(driver)
        base.click_list_order_and_retern_onmain_page()
        assert base.get_current_url() == Urls.BASE_URL

    @allure.title('Проверка кнопки Лента заказов.')
    @allure.description('Нажатие на кнопку Лента заказов выполняется переход на страницу заказов.')
    def test_click_on_list_order(self, driver):
        base = BasicFunctionality(driver)
        base.click_on_list_order()
        assert base.get_current_url() == Urls.LIST_ORDER

    @allure.title('Описание Ингридиента.')
    @allure.description('При нажатий на ингридиента открывается карточка описания ингридиента.')
    def test_open_description_ingredients(self, driver):
        base = BasicFunctionality(driver)
        assert base.click_ingredient_check_displade() == True

    @allure.title('Нажатие на крестик')
    @allure.description('Проверка закрытия карточки ингридиента нажатием на крестик')
    def test_description_ingredients_close_click_by_cross(self, driver):
        base = BasicFunctionality(driver)
        assert base.click_cross_in_description_ingredients_check_displayed() == True

    @allure.title('Добавление ингредиента в заказ')
    @allure.description('Добавление булок в заказ')
    def test_adding_ingredient_to_order_counter_and_ingredient_incremented(self, driver):
        base = BasicFunctionality(driver)
        assert base.move_ingredients_to_order_check_is_displayed() == True

    @allure.title('Оформление заказа авторизированным пользователем')
    @allure.description('Пользователь создан через API им делаем заказ')
    def test_log_in_user_place_an_order(self, driver):
        base = BasicFunctionality(driver)
        base.make_order_login_user()
        assert base.displayed_statys_order() == True
