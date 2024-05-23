from locators.dropdown_page_locators import DropDownPageLocators
from pages.base_page import BasePage
import random
import re
from data.data import Data


class DropdownPage(BasePage):
    locators = DropDownPageLocators()

    def select_dropdown_item(self):
        self.element_is_visible(self.locators.DROPDOWN_BUTTON).click()
        item_list = self.elements_are_visible(self.locators.DROPDOWN_ITEM_LIST)
        item_to_click = item_list[random.randint(0, len(item_list) - 1)]
        item_text = item_to_click.text
        item_to_click.click()
        return item_text

    def check_open_link(self, item):
        open_tab_text = re.split('/', self.driver.current_url)[-1]
        item_name = Data.dropdown_menu.get(item)
        assert open_tab_text == item_name, "link name does not match selected item"
