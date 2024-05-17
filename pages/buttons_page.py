from locators.buttons_page_locators import ButtonsPageLocators
from pages.base_page import BasePage


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def check_all_buttons_clickable(self):
        assert self.element_is_visible(self.locators.PRIMARY_BUTTON).is_enabled()
        assert self.element_is_visible(self.locators.SUCCESS_BUTTON).is_enabled()
        assert self.element_is_visible(self.locators.INFO_BUTTON).is_enabled()
        assert self.element_is_visible(self.locators.WARNING_BUTTON).is_enabled()
        assert self.element_is_visible(self.locators.DANGER_BUTTON).is_enabled()
        assert self.element_is_visible(self.locators.LINK_BUTTON).is_enabled()
        assert self.element_is_visible(self.locators.LEFT_BUTTON).is_enabled()
        assert self.element_is_visible(self.locators.MIDDLE_BUTTON).is_enabled()
        assert self.element_is_visible(self.locators.RIGHT_BUTTON).is_enabled()
        assert self.element_is_visible(self.locators.FIRST_BUTTON).is_enabled()
        assert self.element_is_visible(self.locators.SECOND_BUTTON).is_enabled()
        assert self.element_is_visible(self.locators.DROPDOWN_BUTTON).is_enabled()

    def check_dropdown_items_are_present(self):
        self.element_is_visible(self.locators.DROPDOWN_BUTTON).click()

        assert self.element_is_visible(self.locators.DROPDOWN_LINK_1).is_displayed()
        assert self.element_is_visible(self.locators.DROPDOWN_LINK_2).is_displayed()
