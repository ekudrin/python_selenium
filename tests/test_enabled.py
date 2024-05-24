from pages.enabled_page import EnabledPage


def test_input_availability(driver):
    enable_page = EnabledPage(driver, "https://formy-project.herokuapp.com/enabled")
    enable_page.open()
    enable_page.check_input_availability()