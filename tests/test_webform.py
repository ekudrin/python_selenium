from pages.webform_page import WebFormPage


def test_webform(driver):
    webform_page = WebFormPage(driver, "https://formy-project.herokuapp.com/form")
    webform_page.open()
    webform_page.fill_form()
    webform_page.check_success_message()
