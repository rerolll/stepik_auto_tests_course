"""
# Тут расположено решение тестового задания по курсу
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 3, раздел 2, степ 13
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("Smolensk")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        browser.quit()
        self.assertEqual(
            welcome_text, "Congratulations! You have successfully registered!"
        )

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("Smolensk")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        browser.quit()
        self.assertEqual(
            welcome_text, "Congratulations! You have successfully registered!"
        )


if __name__ == "__main__":
    unittest.main()
