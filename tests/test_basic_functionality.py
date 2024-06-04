from locator.locators import LocatorBaseFunctionality, Locators
from pages.basic_functionality import BasicFunctionality
import time
from urls import Urls


class TestBasicFunctionality:

    def test_click_on_constructor(self, driver):
        base = BasicFunctionality(driver)
        assert base.click_list_order_and_retern_onmain_page() != Urls.BASE_URL

    def test_click_on_list_order(self, driver):
        base = BasicFunctionality(driver)
        assert base.click_on_list_order() == Urls.LIST_ORDER

    def test_open_description_ingredients(self, driver):
        base = BasicFunctionality(driver)
        base.click_ingredients_description()
        assert base.element_is_displayed(LocatorBaseFunctionality.DETAILS_ORDER) == True

    def test_description_ingredients_close_click_by_cross(self, driver):
        base = BasicFunctionality(driver)
        base.click_cross_in_description_ingredients()
        assert base.element_is_displayed(LocatorBaseFunctionality.DETAILS_ORDER) == False

    def test_adding_ingredient_to_order_counter_and_ingredient_incremented(self, driver):
        base = BasicFunctionality(driver)
        base.move_ingredients_to_order()
        assert base.element_is_displayed(LocatorBaseFunctionality.TWO_BUN_COUNTER) == True

    def test_log_in_user_place_an_order(self, driver):
        base = BasicFunctionality(driver)
        base.make_order_login_user()
        assert base.element_is_displayed(LocatorBaseFunctionality.TEXT_ORDER_START_COOK) == True
