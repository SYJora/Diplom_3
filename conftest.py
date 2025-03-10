import pytest
from selenium import webdriver

from urls import Urls


@pytest.fixture(scope='function', params=['firefox', 'chrome'])
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




