'''
# Тут расположено решение тестового задания по курсу
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 2, раздел 4, 7 степ
'''
import math

import pyperclip as pc

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, "#book")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    button1.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = calc(x_element.text)

    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input2.send_keys(x)

    button2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    button2.click()

    pc.copy(browser.switch_to.alert.text.split(': ')[-1])

finally:
    browser.quit()
