from pages.list_order_page import ListOrder


class TestListOrder:

    def test_order_details(self, driver):
        base = ListOrder(driver)
        respons = base.make_oder_api()
        num = respons.json()['order']['number']
        base.enter_to_personal_cabinet()
        base.press_personal_account()
        history_order = base.get_order_from_history(num)
        base.select_list_order()
        assert base.list_order_get_number_order(history_order) == True