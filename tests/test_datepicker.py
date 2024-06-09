import allure

from pages.datepicker_page import DatepickerPage


@allure.feature("Datepicker")
class TestDatepicker:
    @allure.title('Check date picker')
    def test_datepicker(self, driver):
        datepicker_page = DatepickerPage(driver, 'https://formy-project.herokuapp.com/datepicker')
        datepicker_page.open()
        date = datepicker_page.select_date()
        datepicker_page.check_date(date)
