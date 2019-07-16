from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.NAME, "login_submit")
    REGISTER_FORM = (By.NAME, "registration_submit")

class ProductPageLocators (object):
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    SUCCESS_ALERT_WITH_NAME_OF_BOOK = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    SUCCESS_ALERT_WITH_PRICE_OF_BASKET = (By.CSS_SELECTOR, ".alert-info strong")
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, ".btn-group>.btn-default:nth-child(1)")

class CartPageLocators(object):
    BASKET_SUMMARY = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_MESSAGE =(By.CSS_SELECTOR, "#content_inner>p")
