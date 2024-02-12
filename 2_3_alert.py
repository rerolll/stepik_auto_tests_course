'''
# Тут расположено решение тестового задания по курсу
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 2, раздел 3, 4 степ
'''
import math

import pyperclip as pc

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = calc(x_element.text)

    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input2.send_keys(x)

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button2.click()

    pc.copy(browser.switch_to.alert.text.split(': ')[-1])

finally:
    browser.quit()
