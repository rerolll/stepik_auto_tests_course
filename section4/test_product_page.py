import pytest
import time

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        page.open()

        page.go_to_login_page()
        page.register_new_user(email=str(time.time())+"@fakemail.org", password="Psad1wsadSa")
        page.should_be_authorized_user()

    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser)
        page.open()

        page.should_be_button_add_to_basket()
        page.click_button_add_to_basket()

        page.solve_quiz_and_get_code()

        page.should_be_added_book_name_message()
        page.should_be_added_book_name_is_correct()

        page.should_be_added_book_price_message()
        page.should_be_added_book_price_is_correct()

    @pytest.mark.new
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()

        page.should_be_button_add_to_basket()
        page.click_button_add_to_basket()

        page.solve_quiz_and_get_code()

        page.should_be_added_book_name_message()
        page.should_be_added_book_name_is_correct()

        page.should_be_added_book_price_message()
        page.should_be_added_book_price_is_correct()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, timeout=0)
        page.open()

        page.should_be_button_add_to_basket()
        page.click_button_add_to_basket()

        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, timeout=0)
        page.open()

        page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, timeout=0)
        page.open()

        page.should_be_button_add_to_basket()
        page.click_button_add_to_basket()

        page.should_dissapear_of_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, timeout=0)
        page.open()
        page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser)
        page.open()
        page.go_to_basket_page()
        page.should_be_basket_is_empety()
        page.should_be_text_basket_is_empety()
