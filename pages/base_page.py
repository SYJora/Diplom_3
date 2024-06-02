from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random

class GeneralMethods:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def generate_random_word(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def click_by_elemet_locator(self, locator):
        self.driver.find_element(*locator).click()

    def wait_element(self, driver, locator):
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable(locator))

    def element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def insert_data_to_fild(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    def click_ver_ywo(self, driver, locator):
        filter_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator))
        ActionChains(driver).move_to_element(filter_field).click().perform()


    def doubel_click(self, driver, locator):
        clickable = driver.find_element(*locator)
        ActionChains(driver) \
            .double_click(clickable) \
            .perform()
