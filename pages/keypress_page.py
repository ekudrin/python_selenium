import allure

from generator import generator
from locators.keypress_page_locators import KeyPressPageLocators
from pages.base_page import BasePage
import random, string


class KeyPressPage(BasePage):
    locators = KeyPressPageLocators()

    @allure.step("Fill input with text")
    def fill_input(self):
        text_input = self.element_is_visible(self.locators.TEXT_INPUT)
        text_input.click()

        test_string = generator.generated_string()
        text_input.send_keys(test_string)
        return test_string

    @allure.step("Check text in input")
    def check_input_text(self, text):
        actual_text = self.element_is_visible(self.locators.TEXT_INPUT).get_attribute('value')
        assert text == actual_text, 'Text in input is invalid'
