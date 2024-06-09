from selenium.webdriver.common.by import By


class WebFormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    JOB_TITLE = (By.CSS_SELECTOR, "#job-title")
    EDUCATION_LIST = (By.CSS_SELECTOR, "input[type='radio']")
    GENDER_LIST = (By.CSS_SELECTOR, "input[type='checkbox']")
    EXPERIENCE_FIELD = (By.CSS_SELECTOR, "#select-menu")
    EXPERIENCE_OPTION_LIST = (By.CSS_SELECTOR, "option")
    DATE = (By.CSS_SELECTOR, "input#datepicker")
    CURRENT_DATE = (By.XPATH, "//div[@class='datepicker-days']//td[@class='today day']")
    DAYS_LIST = (By.XPATH, "//div[@class='datepicker-days']//tbody//td")
    SUBMIT = (By.CSS_SELECTOR, "a[role='button']")

    # Success page
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div[class='alert alert-success']")
