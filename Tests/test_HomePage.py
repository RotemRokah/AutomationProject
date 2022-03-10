import pytest

from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest


class Test_Home(BaseTest):

    def test_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_search_bar_text(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_book_search("Test")
        text = self.homePage.get_search_bar_text()
        assert text == "Test"


