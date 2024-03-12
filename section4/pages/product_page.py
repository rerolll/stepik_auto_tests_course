import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage

from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_TO_BASCKET
        ), "Login link is not presented"

    def click_button_add_to_basket(self):
        self.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASCKET).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")