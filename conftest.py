import pytest
from selenium import webdriver

from data.data_reset_password import DataCreateUser
from urls import Urls


@pytest.fixture(params=['firefox', 'chrome'], scope='functions')
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.maximize_window()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.maximize_window()

    browser.get(Urls.BASE_URL)

    yield browser

    browser.quit()

@pytest.fixture(params=['firefox', 'chrome'])
def driver_recovery(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()

    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.get(Urls.FORGOT_PASSWORD)

    yield browser

    browser.quit()



