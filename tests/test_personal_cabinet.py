from locator.reset_password_locators import LocatorsResetPasswprd
from pages.base_page import GeneralMethods
from pages.personal_cabinet_page import PersonalCabinet
from urls import Urls
import time


class TestPersonalCabinet:

    def test_click_through_personal_сabinet(self, driver):
        base = GeneralMethods(driver)
        base.click_ver_ywo(driver, LocatorsResetPasswprd.BUTTON_PERSONAL_ACCOUNT)
        assert driver.current_url == Urls.ACOUNT_LOGIN

    def test_click_through_history_order(self, driver):
        base = PersonalCabinet(driver)
        base.log_in_new()
        assert driver.current_url == Urls.ORDER_HISTORY

    def test_log_out_personal_сabine(self, driver):
        base = PersonalCabinet(driver)
        base.log_in_and_out()
        assert driver.current_url == Urls.ACOUNT_LOGIN
