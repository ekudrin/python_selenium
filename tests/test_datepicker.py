from pages.datepicker_page import DatepickerPage


def test_datepicker(driver):
    datepicker_page = DatepickerPage(driver, 'https://formy-project.herokuapp.com/datepicker')
    datepicker_page.open()
    date = datepicker_page.select_date()
    datepicker_page.check_date(date)



