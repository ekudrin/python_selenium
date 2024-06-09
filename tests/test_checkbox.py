import allure

from pages.checkbox_page import CheckboxPage


@allure.feature("Checkbox")
class TestCheckBox:
    @allure.title("Check selected checkbox")
    def test_selected_checkboxes(self,driver):
        checkbox_page = CheckboxPage(driver, 'https://formy-project.herokuapp.com/checkbox')
        checkbox_page.open()
        selected_boxes = checkbox_page.select_checkboxes()
        checkbox_page.check_selected_checkboxes(selected_boxes)
