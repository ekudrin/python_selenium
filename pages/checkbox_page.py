import random

from locators.checkbox_page_locators import CheckboxPageLocators
from pages.base_page import BasePage


class CheckboxPage(BasePage):
    locators = CheckboxPageLocators()

    def select_checkboxes(self):
        checkbox_list = self.elements_are_visible(self.locators.ALL_CHECKBOX)
        random.shuffle(checkbox_list)
        num_of_elements_to_click = random.randint(1, 3)
        selected_checkboxes = []
        for i in range(num_of_elements_to_click):
            checkbox_list[i].click()
            selected_checkboxes.append(checkbox_list[i])
        return selected_checkboxes

    def check_selected_checkboxes(self, checkbox_list):
        for element in checkbox_list:
            assert element.is_selected()
