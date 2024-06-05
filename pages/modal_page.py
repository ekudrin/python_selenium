from locators.modal_page_locators import ModalPageLocators
from pages.base_page import BasePage


class ModalPage(BasePage):
    locators = ModalPageLocators()

    def check_text_in_modal(self):
        self.element_is_visible(self.locators.OPEN_BUTTON).click()
        modal_text = self.element_is_visible(self.locators.MODAL_TEXT).text
        assert modal_text == 'Some text here', 'Incorrect text in window'

    def check_close_button(self):
        self.element_is_visible(self.locators.OPEN_BUTTON).click()
        self.element_is_visible(self.locators.CLOSE_BUTTON).click()
        assert self.element_is_not_visible(self.locators.MODAL_WINDOW)