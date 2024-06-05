import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.data_reset_password import DataResetPassword
from locator.locators import Locators
from pages.base_page import GeneralMethods
from urls import Urls


class TestPasswordReset:

    @allure.title('Тест ссылки востановление пароля.')
    @allure.description('Ссылка для постановления находится в персональном кабинете.')
    def test_password_recovery_page_by_clicking_the_recover_password(self, driver):
        reset_password = GeneralMethods(driver)
        reset_password.click_ver_two(driver, Locators.BUTTON_PERSONAL_ACCOUNT)
        reset_password.click_by_elemet_locator(Locators.LINK_FORGOT_PASSWORD)
        assert reset_password.element_is_displayed(Locators.BUTTON_RESET)

    @allure.title('Тест ввести эмейл и нажать кнопку востановить.')
    @allure.description('Проверка работы поля е-мейла и кнопки восстановить и перехода.')
    def test_enter_email_click_button_recovery(self, driver_recovery):
        base = GeneralMethods(driver_recovery)
        WebDriverWait(driver_recovery, 30).until(EC.presence_of_element_located(Locators.BUTTON_RESET))
        base.insert_data_to_fild(Locators.ACCOUNT_EMAIL, DataResetPassword.email)
        base.click_ver_two(driver_recovery, Locators.BUTTON_RESET)
        WebDriverWait(driver_recovery, 10).until(
            expected_conditions.url_to_be(Urls.RESET_PASSWORD))
        assert driver_recovery.current_url == Urls.RESET_PASSWORD

    @allure.title('Проверка кнопки отображения и скрытия пароля.')
    @allure.description('После нажатия кнопки показать пароль поле становится активным.')
    def test_clicking_show_hide_password_button_makes_field_active(self, driver):
        base = GeneralMethods(driver)
        base.click_ver_two(driver, Locators.BUTTON_PERSONAL_ACCOUNT)
        base.insert_data_to_fild(Locators.ACCOUNT_PASSWORD, '12345')
        base.click_by_elemet_locator(Locators.HIDE_SHOW_PASSWORD)
        assert base.element_is_displayed(Locators.HIDE_SHOW_ELEM) == True


