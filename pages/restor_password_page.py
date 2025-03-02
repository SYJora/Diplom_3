import allure

from data.data_reset_password import DataResetPassword
from locator.locators import Locators
from pages.base_page import BasePage
from urls import Urls


class RestorPassword(BasePage):

    @allure.step('Востановление пароля')
    def clicking_restor_link(self):
        self.find_click_element(Locators.BUTTON_PERSONAL_ACCOUNT)
        self.click_by_elemet_locator(Locators.LINK_FORGOT_PASSWORD)
        return self.element_is_displayed(Locators.BUTTON_RESET)

    @allure.step('Нажатие кнопки востановить пароль')
    def enter_email_and_click_recovery_button(self):
        self.wait_presen_element(Locators.BUTTON_RESET)
        self.insert_data_to_fild(Locators.ACCOUNT_EMAIL, DataResetPassword.email)
        self.find_click_element(Locators.BUTTON_RESET)
        self.wait_urls(Urls.RESET_PASSWORD)

    @allure.step('Нажатие кнопки востановить пароль')
    def get_to_show_hide_password_button(self):
        self.find_click_element(Locators.BUTTON_PERSONAL_ACCOUNT)
        self.insert_data_to_fild(Locators.ACCOUNT_PASSWORD, '12345')
        self.click_by_elemet_locator(Locators.HIDE_SHOW_PASSWORD)
        return self.element_is_displayed(Locators.HIDE_SHOW_ELEM)

    def get_to_url(self):
        self.driver.get(Urls.FORGOT_PASSWORD)