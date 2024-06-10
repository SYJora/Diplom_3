import allure

from pages.personal_cabinet_page import PersonalCabinet
from urls import Urls

class TestPersonalCabinet:

    @allure.title('Проверка кнопки «Личный кабинет»')
    @allure.description('Переход по клику на «Личный кабинет»')
    def test_click_through_personal_сabinet(self, driver):
        base = PersonalCabinet(driver)
        base.click_on_button_personal_account()
        assert base.get_current_url() == Urls.ACOUNT_LOGIN

    @allure.title('Проверка кнопки «История заказов»')
    @allure.description('Переход в раздел «История заказов»')
    def test_click_through_history_order(self, driver):
        base = PersonalCabinet(driver)
        base.log_in_new()
        assert base.get_current_url() == Urls.ORDER_HISTORY

    @allure.title('Проверка выхода из системы')
    @allure.description('Выход из аккаунта')
    def test_log_out_personal_сabine(self, driver):
        base = PersonalCabinet(driver)
        base.log_in_and_out()
        assert base.get_current_url() == Urls.ACOUNT_LOGIN
