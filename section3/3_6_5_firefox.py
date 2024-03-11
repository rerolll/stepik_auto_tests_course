
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://stepik.org/lesson/25969/step/8")

"""https://github.com/SergeyPirogov/webdriver_manager
driver = webdriver.Firefox(executable_path = 'C:/geckodriver')"""
