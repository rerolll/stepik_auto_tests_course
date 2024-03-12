from .pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_to_basket()
    page.click_button_add_to_basket()
    page.solve_quiz_and_get_code()

