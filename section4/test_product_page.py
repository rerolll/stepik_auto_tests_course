import pytest

from .pages.product_page import ProductPage

@pytest.mark.parametrize('promo', range(0, 10))
def test_guest_can_add_product_to_basket(browser, promo):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_to_basket()
    page.click_button_add_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_added_book_name_message()
    page.should_be_added_book_name_is_correct()

    page.should_be_added_book_price_message()
    page.should_be_added_book_price_is_correct()
