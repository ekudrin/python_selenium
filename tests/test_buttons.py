import time
from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, 'https://formy-project.herokuapp.com/')
    page.open()
