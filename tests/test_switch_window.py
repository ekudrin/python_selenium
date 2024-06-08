from pages.test_switch_window_page import SwitchWindowPage


def test_switch_tab(driver):
    switch_page = SwitchWindowPage(driver, "https://formy-project.herokuapp.com/switch-window")
    switch_page.open()
    switch_page.check_new_tab_url()


def test_alert(driver):
    switch_page = SwitchWindowPage(driver, "https://formy-project.herokuapp.com/switch-window")
    switch_page.open()
    switch_page.check_alert_text()
