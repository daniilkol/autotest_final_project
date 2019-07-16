from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def go_to_alert_after_add_button(self):
        link=self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        link.click()

    def check_success_alert_about_name(self):
        product=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name=product.text
        product_alert=self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT_WITH_NAME_OF_BOOK)
        product_alert_name=product_alert.text
        assert product_alert_name == product_name, "Name in success alert and product name does not equal"

    def check_success_alert_about_price_of_basket(self):
        product=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price=product.text
        product_alert=self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT_WITH_PRICE_OF_BASKET)
        product_alert_price=product_alert.text
        assert product_alert_price == product_price, "Price in success alert and product price does not equal"

    def add_to_basket(self):
        link=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def should_not_be_success_message_v_1(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_v_2(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


