import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")

    result = int(x_element.text) + int(y_element.text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()


finally:

    time.sleep(10)
    browser.quit()
