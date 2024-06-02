from selenium.webdriver.common.by import By

class LocatorsResetPasswprd:

    LOGO = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']/child::a")  # Логотип на главной страницы
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")# Кнопка входа в личный кабинет
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(), 'Выход')]")  # Кнопка выхода из личного кабинета
    LINK_FORGOT_PASSWORD = (By.XPATH, "//a[contains(@href, '/forgot')]")
    BUTTON_RESET = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    RESTOR_LOG_TEXT = (By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ACCOUNT_EMAIL = (
    By.XPATH, "//label[contains(text(), 'Email')]/parent::div/child::input"
    )  # Поле ввода электроной почты
    ACCOUNT_PASSWORD = (By.XPATH, "//input[@type = 'password']")  # Поле ввода пароля
    HIDE_SHOW_PASSWORD = (By.XPATH, "//div[@class = 'input__icon input__icon-action']")
    ACCOUNT_PASSWORD = (By.XPATH, "//input[@type = 'password']")  # Поле ввода пароля
    LINK_HISTORY_ORDER = (By.XPATH, "//a[@href = '/account/order-history']") # Сылка на Историю заказов личном кабинете

