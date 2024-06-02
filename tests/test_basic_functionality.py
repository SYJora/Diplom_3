from pages.basic_functionality import BasicFunctionality
from urls import Urls


class TestBasicFunctionality:

    def test_click_on_constructor(self, driver):
        base = BasicFunctionality(driver)
        assert base.click_list_order_and_retern_onmain_page() != Urls.BASE_URL

    def test_click_on_list_order(self, driver):
        base = BasicFunctionality(driver)
        assert base.click_on_list_order() == Urls.LIST_ORDER
