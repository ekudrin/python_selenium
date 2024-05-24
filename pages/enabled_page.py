from locators.enabled_page_locators import EnabledPageLocators
from pages.base_page import BasePage


class EnabledPage(BasePage):
    locators = EnabledPageLocators()

    def check_input_availability(self):
        disabled_input = self.element_is_visible(self.locators.DISABLED_INPUT)
        enabled_input = self.element_is_visible(self.locators.INPUT)
        assert not disabled_input.is_enabled(), "Element should be disabled"
        assert disabled_input.get_attribute('placeholder') == "Disabled input here...", "Element text does not match"
        assert enabled_input.is_enabled(), "Element should be enabled"
        assert enabled_input.get_attribute('placeholder') == "Input here...", "Element text does not match"
