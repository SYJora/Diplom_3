from locator.locators import LocatorListOrder
from pages.list_order_page import ListOrder


class TestListOrder:

    def test_click_order_open_description(self, driver):
        base = ListOrder(driver)
        base.select_first_order_in_list()
        result = base.element_is_displayed(LocatorListOrder.TEXT_IN_DESCRIPTION_CARD)
        assert result == True

    def test_order_in_history_displayed_in_list_order(self, driver):
        base = ListOrder(driver)
        respons = base.make_oder_api()
        num = respons.json()['order']['number']
        base.enter_to_personal_cabinet(respons.json()['order']['owner']['email'])
        base.press_personal_account()
        history_order = base.get_order_from_history(num)
        base.select_list_order()
        assert base.list_order_get_number_order(history_order) == True

    def test_count_of_common_count(self, driver):
        base = ListOrder(driver)
        base.select_list_order()
        befor = base.get_text_from_element(LocatorListOrder.COUNT_DEFOULT)
        base.make_oder_api()
        assert base.get_text_from_element(LocatorListOrder.COUNT_DEFOULT) != befor

    def test_count_done_order(self, driver):
        base = ListOrder(driver)
        base.select_list_order()
        befor = base.get_text_from_element(LocatorListOrder.DONE_COUNT)
        base.make_oder_api()
        assert base.get_text_from_element(LocatorListOrder.DONE_COUNT) != befor

    def test_check_number_in_work(self, driver):
        base = ListOrder(driver)
        assert base.creat_user_add_ingredirnts() != 'Все текущие заказы готовы'




