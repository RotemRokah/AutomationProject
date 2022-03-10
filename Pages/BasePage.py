from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
# import TakeScreenshot
# edit
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#  end edit

"""This class is the parent of all pages"""
"""it contains all the generic methods and utilities for all the pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_element_attribute(self, by_locator, attribute):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute)

    # def get_element_text(self, by_locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     return element.text

    # def get_element_text(self, by_locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     return element.text
    #
    # def do_click(self, by_locator):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
    #
    # def is_enabled(self, by_locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     return bool(element)




