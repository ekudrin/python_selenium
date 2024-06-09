import allure

from pages.enabled_page import EnabledPage


@allure.feature("Enabled")
class TestEnabled:
    @allure.title("Check input")
    def test_input_availability(self,driver):
        enable_page = EnabledPage(driver, "https://formy-project.herokuapp.com/enabled")
        enable_page.open()
        enable_page.check_input_availability()