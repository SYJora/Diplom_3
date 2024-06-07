import allure
from pages.restor_password_page import RestorPassword
from urls import Urls


class TestPasswordReset:

    @allure.title('Тест ссылки востановление пароля.')
    @allure.description('Ссылка для постановления находится в персональном кабинете.')
    def test_password_recovery_page_by_clicking_the_recover_password(self, driver):
        reset_password = RestorPassword(driver)
        result = reset_password.clicking_restor_link()
        assert result == True


    @allure.title('Тест ввести эмейл и нажать кнопку востановить.')
    @allure.description('Проверка работы поля е-мейла и кнопки восстановить и перехода.')
    def test_enter_email_click_button_recovery(self, driver):
        driver.get(Urls.FORGOT_PASSWORD)
        base = RestorPassword(driver)
        base.enter_email_and_click_recovery_button()
        assert driver.current_url == Urls.RESET_PASSWORD

    @allure.title('Проверка кнопки отображения и скрытия пароля.')
    @allure.description('После нажатия кнопки показать пароль поле становится активным.')
    def test_clicking_show_hide_password_button_makes_field_active(self, driver):
        base = RestorPassword(driver)
        assert base.get_to_show_hide_password_button() == True



