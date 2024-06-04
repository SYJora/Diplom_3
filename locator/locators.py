from selenium.webdriver.common.by import By

class Locators:

    LOGO = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']/child::a")  # Логотип на главной страницы
    BUTTON_LIST_ORDER = (By.XPATH, "//p[contains(text(), 'Лента')]")
    BUTTON_DESIGNER = (By.XPATH, "//p[contains(text(), 'Конструктор')]")  # Кнопка перехода в конструктор
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
    TEST = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")

class LocatorBaseFunctionality:
    LIST_ORDER = (By.XPATH, "//h1[@class = 'text text_type_main-large mt-10 mb-5']") # Надпесь в Лента заказов
    IMG_BUN = (By.XPATH, "//img[@src = 'https://code.s3.yandex.net/react/code/bun-01.png']")
    DETAILS_ORDER = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    BUTTON_CROSS = (By.XPATH, "//div[@class = 'Modal_modal__contentBox__sCy8X pt-10 pb-15']/following-sibling::button") # Крестик в описаний ингридиента
    TWO_BUN_COUNTER = (By.XPATH, "//div[@class = 'counter_counter__ZNLkj counter_default__28sqi']/descendant::p[contains(text(), '2')]")
    UP_BUN = (By.XPATH, "//span[contains(text(), 'Перетяните булочку сюда (верх)')]")
    TEXT_ORDER_START_COOK = (By.XPATH, "//p[contains(text(), 'Ваш заказ начали готовить')]")
