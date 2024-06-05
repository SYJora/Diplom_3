import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random


class GeneralMethods:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Возвращает найденный элемент')
    def look_for_locator(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Нажимает на элемент локатора')
    def click_by_elemet_locator(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Элемент можно нажать')
    def wait_element(self, driver, locator):
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable(locator))

    @allure.step('Ожидает появление текста в элементе')
    def wait_text_in_element(self, locator, text):
        WebDriverWait(self.driver, 25).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step('Подтверждение отображения элемента')
    def element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Отправка значения в поле')
    def insert_data_to_fild(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    @allure.step('Ожидание элемента. Передвижение к элементу и нажатие')
    def click_ver_two(self, driver, locator):
        filter_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator))
        ActionChains(driver).move_to_element(filter_field).click().perform()

    @allure.step('Ожидание элемента пока он станет активным и возврат его положения')
    def wait_and_search_element(self, driver, locator):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator))
        return driver.find_element(*locator)

    @allure.step('Получение текста из локатора')
    def get_text_from_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).text

    @allure.step('Двойнок нажатие')
    def doubel_click(self, driver, locator):
        clickable = driver.find_element(*locator)
        ActionChains(driver) \
            .double_click(clickable) \
            .perform()

