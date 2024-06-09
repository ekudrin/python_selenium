import allure

from generator import generator
from locators.page_scroll_page_locators import PageScrollPageLocators
from pages.base_page import BasePage


class PageScrollPage(BasePage):
    locators = PageScrollPageLocators()

    @allure.step("Fill text fields")
    def fill_text_fields(self):
        name_locator = self.element_is_present(self.locators.FULL_NAME_FIELD)
        self.go_to_element(name_locator)
        full_name = self.element_is_visible(self.locators.FULL_NAME_FIELD)
        date = self.element_is_visible(self.locators.DATE_FIELD)

        full_name_text = generator.generated_string()
        date_text = generator.generated_string()

        full_name.send_keys(full_name_text)
        date.send_keys(date_text)
        return full_name_text, date_text

    @allure.step("Check text in fields")
    def check_fields(self, name, date):
        full_name = self.element_is_present(self.locators.FULL_NAME_FIELD).get_attribute('value')
        input_date = self.element_is_present(self.locators.DATE_FIELD).get_attribute('value')
        assert name == full_name
        assert date == input_date
