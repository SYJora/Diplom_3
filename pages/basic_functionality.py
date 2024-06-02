from locator.locators import Locators, LocatorBaseFunctionality
from pages.base_page import GeneralMethods


class BasicFunctionality(GeneralMethods):

    def click_list_order_and_retern_onmain_page(self):
        self.click_ver_ywo(self.driver, Locators.BUTTON_LIST_ORDER)
        self.wait_element(self.driver, LocatorBaseFunctionality.LIST_ORDER)
        urlds = self.driver.current_url
        self.click_ver_ywo(self.driver, Locators.BUTTON_DESIGNER)
        return urlds

    def click_on_list_order(self):
        self.click_ver_ywo(self.driver, Locators.BUTTON_LIST_ORDER)
        self.wait_element(self.driver, LocatorBaseFunctionality.LIST_ORDER)
        urlds = self.driver.current_url
        return urlds