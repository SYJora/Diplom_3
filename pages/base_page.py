import string
import random

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Возвращает найденный элемент')
    def look_for_locator(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Нажимает на элемент локатора')
    def click_by_elemet_locator(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Элемент можно нажать')
    def wait_element(self, locator):
        return WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locator))

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
    def find_click_element(self, locator):
        filter_field = self.wait_element(locator)
        ActionChains(self.driver).move_to_element(filter_field).click().perform()

    @allure.step('Ожидание элемента пока он станет активным и возврат его положения')
    def wait_and_search_element(self, locator):
        self.wait_element(locator)
        return self.look_for_locator(locator)

    @allure.step('Ожидаю невтидемого элемента')
    def wait_invizibel_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))

    @allure.step('Ожедает пока не проподет элемент локатора')
    def wait_until_not_visibl(self, locator):
        WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located(locator))

    @allure.step('Ожедание URLS')
    def wait_urls(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(locator))

    @allure.step('Ожидаем поевления элемента')
    def wait_presen_element(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(locator))

    @allure.step('Получение текста из локатора')
    def get_text_from_element(self, locator):
        self.wait_element(locator)
        return self.driver.find_element(*locator).text

    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Генерация данных')
    def generate_random_word(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @allure.step('Нажимает кнопку ESCAPE на клавиатуре')
    def click_escepe(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()


