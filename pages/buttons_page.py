from locators.buttons_page_locators import ButtonsPageLocators
from pages.base_page import BasePage


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def check_all_buttons_clickable(self):
        assert self.element_is_visible(self.locators.PRIMARY_BUTTON).is_enabled(), "Primary button is not enabled"
        assert self.element_is_visible(self.locators.SUCCESS_BUTTON).is_enabled(), "Success button is not enabled"
        assert self.element_is_visible(self.locators.INFO_BUTTON).is_enabled(), "Info button is not enabled"
        assert self.element_is_visible(self.locators.WARNING_BUTTON).is_enabled(), "Warning button is not enabled"
        assert self.element_is_visible(self.locators.DANGER_BUTTON).is_enabled(), "Danger button is not enabled"
        assert self.element_is_visible(self.locators.LINK_BUTTON).is_enabled(), "Link button is not enabled"
        assert self.element_is_visible(self.locators.LEFT_BUTTON).is_enabled(), "Left button is not enabled"
        assert self.element_is_visible(self.locators.MIDDLE_BUTTON).is_enabled(), "Middle button is not enabled"
        assert self.element_is_visible(self.locators.RIGHT_BUTTON).is_enabled(), "Right button is not enabled"
        assert self.element_is_visible(self.locators.FIRST_BUTTON).is_enabled(), "First button is not enabled"
        assert self.element_is_visible(self.locators.SECOND_BUTTON).is_enabled(), "Second button is not enabled"
        assert self.element_is_visible(self.locators.DROPDOWN_BUTTON).is_enabled(), "Dropdown button is not enabled"

    def check_dropdown_items_are_present(self):
        self.element_is_visible(self.locators.DROPDOWN_BUTTON).click()

        assert self.element_is_visible(self.locators.DROPDOWN_LINK_1).is_displayed(), "Link 1 is not displayed"
        assert self.element_is_visible(self.locators.DROPDOWN_LINK_2).is_displayed(), "Link 2 is not displayed"
