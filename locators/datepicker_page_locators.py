from selenium.webdriver.common.by import By


class DatepickerPageLocators:
    DATEPICKER_INPUT = (By.XPATH, "//input[@id='datepicker']")
    MONTH_SELECTOR = (By.XPATH, "//div[@class='datepicker-days']//th[@class='datepicker-switch']")
    YEAR_SELECTOR = (By.XPATH, "//div[@class='datepicker-months']//th[@class='datepicker-switch']")
    YEAR_LIST = (By.XPATH, "//div[@class='datepicker-years']//span")
    MONTH_LIST = (By.XPATH, "//div[@class='datepicker-months']//span")
    DAYS_LIST = (By.XPATH, "//div[@class='datepicker-days']//td[@class='day']")

