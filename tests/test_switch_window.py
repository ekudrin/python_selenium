import allure

from pages.switch_window_page import SwitchWindowPage


@allure.feature("Switch Window")
class TestSwitchWindow:
    @allure.title("Open new tab")
    def test_switch_tab(self, driver):
        switch_page = SwitchWindowPage(driver, "https://formy-project.herokuapp.com/switch-window")
        switch_page.open()
        switch_page.check_new_tab_url()

    @allure.title("Open alert")
    def test_alert(self, driver):
        switch_page = SwitchWindowPage(driver, "https://formy-project.herokuapp.com/switch-window")
        switch_page.open()
        switch_page.check_alert_text()
