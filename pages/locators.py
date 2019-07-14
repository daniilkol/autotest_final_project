from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.NAME, "login_submit")
    REGISTER_FORM = (By.NAME, "registration_submit")

class ProductPageLocators (object):
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME =(By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    SUCCESS_ALERT_WITH_NAME_OF_BOOK =(By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    SUCCESS_ALERT_WITH_PRICE_OF_BASKET =(By.CSS_SELECTOR, ".alert-info strong")