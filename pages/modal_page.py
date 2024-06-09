import time

import allure

from locators.modal_page_locators import ModalPageLocators
from pages.base_page import BasePage


class ModalPage(BasePage):
    locators = ModalPageLocators()

    @allure.step("Check text in modal")
    def check_text_in_modal(self):
        self.element_is_visible(self.locators.OPEN_BUTTON).click()
        modal_text = self.element_is_visible(self.locators.MODAL_TEXT).text
        assert modal_text == 'Some text here', 'Incorrect text in window'

    @allure.step("Check close button in modal")
    def check_close_button(self):
        self.element_is_visible(self.locators.OPEN_BUTTON).click()
        modal_window = self.element_is_visible(self.locators.MODAL_WINDOW)
        self.element_is_visible(self.locators.CLOSE_BUTTON).click()
        time.sleep(1)
        assert not modal_window.is_displayed()
