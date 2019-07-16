from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest
import time


class TestUserAddToCartFromProductPage(object):

    @pytest.fixture(scope="function",autouse=True)
    def setup(self,browser):
        link="http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page=LoginPage(browser,link)
        page.open()
        page.register_new_user(email=str(time.time())+"@fakemail.org",password=str(time.time()))
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page=ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message_v_1()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self,browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page=ProductPage(browser,link)
        page.open()
        page.go_to_alert_after_add_button()
        page.solve_quiz_and_get_code()
        page.check_success_alert_about_name()
        page.check_success_alert_about_price_of_basket()


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page=ProductPage(browser,link)
    page.open()
    page.go_to_alert_after_add_button()
    page.solve_quiz_and_get_code()
    page.check_success_alert_about_name()
    page.check_success_alert_about_price_of_basket()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page=ProductPage(browser,link)
    page.open()
    page.go_to_cart_page()
    cart_page=CartPage(browser,browser.current_url)
    cart_page.check_cart_is_empty()
    cart_page.should_be_cart_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page=ProductPage(browser,link)
    page.open()
    page.go_to_login_page()
    login_page=LoginPage(browser,browser.current_url)
    login_page.should_be_login_page()
