import random

import allure

from locators.datepicker_page_locators import DatepickerPageLocators
from pages.base_page import BasePage
import calendar
from data.data import Data


class DatepickerPage(BasePage):
    locators = DatepickerPageLocators()

    @allure.step("Select date from datepicker")
    def select_date(self):
        month_dict = Data.month_dict

        self.element_is_visible(self.locators.DATEPICKER_INPUT).click()
        self.element_is_visible(self.locators.MONTH_SELECTOR).click()
        self.element_is_visible(self.locators.YEAR_SELECTOR).click()

        year_list = self.elements_are_visible(self.locators.YEAR_LIST)
        selected_year = year_list[random.randint(0, (len(year_list) - 1))]
        year_text = selected_year.text
        selected_year.click()

        month_list = self.elements_are_visible(self.locators.MONTH_LIST)
        selected_month = month_list[random.randint(0, (len(month_list) - 1))]
        for key, value in month_dict.items():
            if selected_month.text == value:
                month_text = key

        selected_month.click()

        days_list = self.elements_are_visible(self.locators.DAYS_LIST)
        selected_day = days_list[random.randint(0, len(days_list) - 1)]
        day_text = selected_day.text
        if len(day_text) == 1:
            day_text = day_text.zfill(2)
        selected_day.click()

        return month_text, day_text, year_text,

    @allure.step("Check date in field")
    def check_date(self, date):
        input_text = self.element_is_visible(self.locators.DATEPICKER_INPUT).get_attribute('value')
        date_value = "{}/{}/{}".format(date[0], date[1], date[2])
        assert input_text == date_value, "value in input field is incorrect"
