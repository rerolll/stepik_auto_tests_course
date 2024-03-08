import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from temp import email, password
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def auth_class(browser):
    sign_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login"))
    )
    sign_button.click()

    browser.find_element(
        By.CSS_SELECTOR, "#id_login_email").send_keys(email)
    browser.find_element(
        By.CSS_SELECTOR, "#id_login_password").send_keys(password)
    browser.find_element(
        By.CSS_SELECTOR, "button.sign-form__btn").click()