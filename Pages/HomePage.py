from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    """By locators - OR"""
    SEARCH_BAR = (By.ID, "searchBar")

    """constructor of the page class """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """this is used to get the page title"""
    def get_Home_page_title(self, title):
        return self.get_title(title)

    """this is used to search for a book"""
    def do_book_search(self, book_name):
        self.do_send_keys(self.SEARCH_BAR, book_name)

    """this is used to get the text in the searchbar"""
    def get_search_bar_text(self):
        return self.get_element_attribute(self.SEARCH_BAR, "value")


