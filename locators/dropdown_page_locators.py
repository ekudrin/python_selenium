from selenium.webdriver.common.by import By


class DropDownPageLocators:
    DROPDOWN_BUTTON = (By.XPATH, "//button[@id='dropdownMenuButton']")
    DROPDOWN_ITEM_LIST = (By.XPATH, "//div[@class='dropdown-menu show']/a[@class='dropdown-item']")
