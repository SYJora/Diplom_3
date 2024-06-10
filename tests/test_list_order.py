import allure

from locator.locators import LocatorListOrder
from pages.list_order_page import ListOrder


class TestListOrder:

    @allure.title('Открыть описание заказа')
    @allure.description('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_open_description(self, driver):
        base = ListOrder(driver)
        result = base.select_first_order_in_list()
        assert result == True

    @allure.title('Отображение историй заказов')
    @allure.description('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_in_history_displayed_in_list_order(self, driver):
        base = ListOrder(driver)
        history_order = base.check_order_in_history_and_list_order()
        list_order = base.list_order_get_number_order()
        assert history_order == list_order

    @allure.title('Проверка счетчика выполнено за все время')
    @allure.description('При создании нового заказа счётчик Выполнено за всё время увеличивается,')
    def test_count_of_common_count(self, driver):
        base = ListOrder(driver)
        befor = base.get_count_of_common()
        current_count = base.make_order_and_returncurrent_count()
        assert befor != current_count.split('\n')


    @allure.title('Проверка счетчика выполнено за сегодня')
    @allure.description('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_count_done_order(self, driver):
        base = ListOrder(driver)
        befor = base.get_count_make_burger_a_day()
        current_count = base.get_new_count_make_burger_a_day()
        assert befor != current_count

    @allure.title('Номер заказа появляется в строке в работе')
    @allure.description('После оформления заказа его номер появляется в разделе В работе')
    def test_check_number_in_work(self, driver):
        base = ListOrder(driver)
        assert base.creat_user_add_ingredirnts() != 'Все текущие заказы готовы'




