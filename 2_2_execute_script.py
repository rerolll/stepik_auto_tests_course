import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = calc(x_element.text)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(x)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    button.click()


finally:

    time.sleep(10)
    browser.quit()
