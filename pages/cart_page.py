from .base_page import BasePage
from .locators import CartPageLocators
from selenium.webdriver.common.by import By

class CartPage(BasePage):

    def check_cart_is_empty(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_SUMMARY), \
            "Your basket is not empty, but should be"

    def should_be_cart_message(self):
        message_link=self.browser.find_element(*CartPageLocators.BASKET_MESSAGE)
        message=message_link.text
        assert "Your basket is empty." in message, \
            "There is no basket empty message, something wrong"


