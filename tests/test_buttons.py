import allure

from pages.buttons_page import ButtonsPage


@allure.feature("Buttons")
class TestButtons:
    @allure.title("Check clickable buttons")
    def test_clickable_buttons(self, driver):
        buttons_page = ButtonsPage(driver, 'https://formy-project.herokuapp.com/buttons')
        buttons_page.open()
        buttons_page.check_all_buttons_clickable()

    @allure.title("Check dropdown")
    def test_dropdown_items_present(self, driver):
        buttons_page = ButtonsPage(driver, 'https://formy-project.herokuapp.com/buttons')
        buttons_page.open()
        buttons_page.check_dropdown_items_are_present()
