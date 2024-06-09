import allure

from locators.dragdrop_page_locators import DragdropPageLocators
from pages.base_page import BasePage


class DragdropPage(BasePage):
    locators = DragdropPageLocators()

    @allure.step("Drag and drop image")
    def drag_n_drop_image(self):
        self.drag_n_drop_to_element(self.element_is_visible(self.locators.IMAGE),
                                    self.element_is_visible(self.locators.DROPBOX))

    @allure.step("Check dropbox message")
    def check_dropbox_text(self):
        assert self.element_is_visible(self.locators.DROPBOX_TEXT).text == 'Dropped!', "Text in dropbox is invalid"

