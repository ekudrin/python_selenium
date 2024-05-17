from selenium.webdriver.common.by import By


class ButtonsPageLocators:
    PRIMARY_BUTTON = (By.XPATH, "//button[text()='Primary']")
    SUCCESS_BUTTON = (By.XPATH, "//button[text()='Success']")
    INFO_BUTTON = (By.XPATH, "//button[text()='Info']")
    WARNING_BUTTON = (By.XPATH, "//button[text()='Warning']")
    DANGER_BUTTON = (By.XPATH, "//button[text()='Danger']")
    LINK_BUTTON = (By.XPATH, "//button[text()='Link']")
    LEFT_BUTTON = (By.XPATH, "//button[text()='Left']")
    MIDDLE_BUTTON = (By.XPATH, "//button[text()='Middle']")
    RIGHT_BUTTON = (By.XPATH, "//button[text()='Right']")
    FIRST_BUTTON = (By.XPATH, "//button[text()='Right']")
    SECOND_BUTTON = (By.XPATH, "//button[text()='Right']")
    DROPDOWN_BUTTON = (By.XPATH, "//button[@id='btnGroupDrop1']")
    DROPDOWN_LINK_1 = (By.XPATH, "//a[text()='Dropdown link 1']")
    DROPDOWN_LINK_2 = (By.XPATH, "//a[text()='Dropdown link 2']")
