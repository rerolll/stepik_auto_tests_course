from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_EMPETY = (By.CSS_SELECTOR, "form#basket_formset.basket_summary")
    BASKET_EMPETY_TEXT = (By.XPATH, "//p[contains(text(), 'empty')]")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGESTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGESTRATION_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGESTRATION_FORM_PASSWORD1 = (
        By.CSS_SELECTOR,
        "#id_registration-password1",
    )
    REGESTRATION_FORM_PASSWORD2 = (
        By.CSS_SELECTOR,
        "#id_registration-password2",
    )
    REGESTRATION_FORM_BUTTON = (
        By.CSS_SELECTOR,
        "[name='registration_submit']",
    )
    REGESTRATION_ALERT_SUCCESS = (By.CSS_SELECTOR, "div.alert.alert-success")


class ProductPageLocators:
    BUTTON_ADD_TO_BASCKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_ADD_PRODUCT = (
        By.CSS_SELECTOR,
        ".alert-safe:nth-of-type(1) .alertinner strong",
    )
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    MESSAGE_ADD_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        ".alert-info .alertinner strong",
    )
