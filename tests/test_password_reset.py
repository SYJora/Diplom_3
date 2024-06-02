from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.data_reset_password import DataResetPassword
from locator.locators import Locators
from pages.base_page import GeneralMethods
from urls import Urls


class TestPasswordReset:

    def test_password_recovery_page_by_clicking_the_recover_password(self, driver):
        reset_password = GeneralMethods(driver)
        WebDriverWait(driver, 30).until(
            expected_conditions.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT))
        reset_password.click_by_elemet_locator(Locators.BUTTON_PERSONAL_ACCOUNT)
        reset_password.click_by_elemet_locator(Locators.LINK_FORGOT_PASSWORD)
        assert reset_password.element_is_displayed(Locators.BUTTON_RESET)

    def test_enter_email_click_button_recovery(self, driver_recovery):
        base = GeneralMethods(driver_recovery)
        WebDriverWait(driver_recovery, 30).until(EC.presence_of_element_located(Locators.BUTTON_RESET))
        base.insert_data_to_fild(Locators.ACCOUNT_EMAIL, DataResetPassword.email)
        base.click_ver_ywo(driver_recovery, Locators.BUTTON_RESET)
        WebDriverWait(driver_recovery, 10).until(
            expected_conditions.url_to_be(Urls.RESET_PASSWORD))
        assert driver_recovery.current_url == Urls.RESET_PASSWORD

    def test_clicking_show_hide_password_button_makes_field_active(self, driver):
        base = GeneralMethods(driver)
        WebDriverWait(driver, 30).until(
            expected_conditions.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT))
        base.click_by_elemet_locator(Locators.BUTTON_PERSONAL_ACCOUNT)
        base.insert_data_to_fild(Locators.ACCOUNT_PASSWORD, '12345')
        base.click_by_elemet_locator(Locators.HIDE_SHOW_PASSWORD)
        text = driver.find_element(By.ID, "text").text
        assert text == True


