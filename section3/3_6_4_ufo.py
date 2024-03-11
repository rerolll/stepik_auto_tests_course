import pytest
import time
import math
from temp import email, password

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


links = [  # Список ссылок на тестируемые страницы
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


@pytest.fixture(scope="function")
def answer():
    return str(math.log(int(time.time())))


class TestStepik:
    authenticated = False
    result = ""

    @classmethod
    def setup_class(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)

    @staticmethod
    def auth_class(browser):
        sign_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    ".ember-view.navbar__auth.navbar__auth_login",
                )
            )
        )
        sign_button.click()

        browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(
            email
        )
        browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(
            password
        )
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

    @classmethod
    def teardown_class(cls):
        """Метод класса закрывает браузер"""
        cls.browser.quit()
        print("\n", TestStepik.result)

    @pytest.mark.parametrize("link", links)
    def test_stepik(self, link, answer):
        self.browser.get(link)

        if not TestStepik.authenticated:
            self.auth_class(self.browser)
            TestStepik.authenticated = True

        try:
            again_button = self.browser.find_element(
                By.CSS_SELECTOR, "button.again-btn"
            )
            again_button.click()

            print('Кнопка "Решить снова" обнаружена')

        except NoSuchElementException:
            print('Кнопка "Решить снова" не обнаружена')

        finally:
            WebDriverWait(self.browser, 10).until_not(
                EC.element_attribute_to_include(
                    (By.CSS_SELECTOR, "textarea.ember-text-area"), "disabled"
                )
            )
            textarea = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
            )
            textarea.send_keys(answer)

            submit_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.submit-submission")
                )
            )
            submit_button.click()

            feedback = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "p.smart-hints__hint")
                )
            )

            try:
                assert feedback.text == "Correct!"

            except AssertionError:
                TestStepik.result += self.browser.find_element(
                    By.CSS_SELECTOR, "p.smart-hints__hint"
                ).text
