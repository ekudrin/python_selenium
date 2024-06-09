import random

import allure

from locators.radiobutton_page_locators import RadioButtonPageLocators
from pages.base_page import BasePage


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step("Select random button")
    def select_random_button(self):
        radiobutton_list = self.elements_are_visible(self.locators.RADIOBUTTON_LIST)
        selected_button = radiobutton_list[random.randint(0, 2)]
        selected_button.click()
        return radiobutton_list, selected_button

    @allure.step("Check which button is selected")
    def check_selected_radiobutton(self, button_list, selected_element):
        for element in button_list:
            if element == selected_element:
                assert element.is_selected()
            else:
                assert not element.is_selected()
