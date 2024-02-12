"""
# Тут расположено решение тестового задания по курсу
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 3, раздел 2, степ 13
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(
        By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")

    browser.find_element(
        By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")

    browser.find_element(
        By.CSS_SELECTOR, ".first_block .third").send_keys("Smolensk")

    browser.find_element(
        By.CSS_SELECTOR, "button.btn").click()

    return browser.find_element(By.TAG_NAME, "h1").text


class TestAbs(unittest.TestCase):

    def test_1(self):
        self.assertEqual(
            link_t("http://suninjuly.github.io/registration1.html"),
            "Congratulations! You have successfully registered!",
            "registration is failed",
        )

    def test_2(self):
        self.assertEqual(
            link_t("http://suninjuly.github.io/registration2.html"),
            "Congratulations! You have successfully registered!",
            "registration is failed",
        )


if __name__ == "__main__":
    unittest.main()
