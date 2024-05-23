from pages.dropdown_page import DropdownPage


def test_dropdown(driver):
    dropdownpage = DropdownPage(driver, "https://formy-project.herokuapp.com/dropdown")
    dropdownpage.open()
    item = dropdownpage.select_dropdown_item()
    dropdownpage.check_open_link(item)
