import allure

from pages.dropdown_page import DropdownPage


@allure.feature("Dropdown")
class TestDropdown:
    @allure.title("Check dropdown list")
    def test_dropdown(self,driver):
        dropdownpage = DropdownPage(driver, "https://formy-project.herokuapp.com/dropdown")
        dropdownpage.open()
        item = dropdownpage.select_dropdown_item()
        dropdownpage.check_open_link(item)
