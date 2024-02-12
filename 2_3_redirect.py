import math

import pyperclip as pc

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(
        By.CSS_SELECTOR, "button.trollface.btn.btn-primary")
    button1.click()

    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = calc(x_element.text)

    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input2.send_keys(x)

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button2.click()

    pc.copy(browser.switch_to.alert.text.split(': ')[-1])

finally:
    browser.quit()
