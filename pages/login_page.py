from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url=self.browser.current_url
        assert "/login" in current_url, "Current url is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented on the login url"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented on the login url"

    def register_new_user (self,email,password):
        input_email=self.browser.find_element (*LoginPageLocators.EMAIL_REGISTRATION_FORM)
        input_email.send_keys(email)
        input_password=self.browser.find_element (*LoginPageLocators.PASSWORD_REGISTRATION_FORM_1)
        input_password.send_keys(password)
        input_password_second_time=self.browser.find_element (*LoginPageLocators.PASSWORD_REGISTRATION_FORM_2)
        input_password_second_time.send_keys(password)
        submit_register=self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        submit_register.click()
