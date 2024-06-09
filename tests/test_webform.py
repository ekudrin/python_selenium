import allure

from pages.webform_page import WebFormPage


@allure.feature("Complete WebForm")
class TestWebForm:
    @allure.title("Submit correct data")
    def test_webform(self,driver):
        webform_page = WebFormPage(driver, "https://formy-project.herokuapp.com/form")
        webform_page.open()
        webform_page.fill_form()
        webform_page.check_success_message()
