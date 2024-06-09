import allure

from locators.switch_window_page_locators import SwitchWindowPageLocators
from pages.base_page import BasePage


class SwitchWindowPage(BasePage):
    locators = SwitchWindowPageLocators()

    @allure.step("Check opened tab url")
    def check_new_tab_url(self):
        self.element_is_visible(self.locators.OPEN_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == "https://formy-project.herokuapp.com/", "Url is incorrect"

    @allure.step("Check text in alert window")
    def check_alert_text(self):
        self.element_is_visible(self.locators.OPEN_ALERT_BUTTON).click()
        alert_text = self.driver.switch_to.alert.text
        assert alert_text == "This is a test alert!", "Alert text in incorrect"





