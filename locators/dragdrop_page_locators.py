from selenium.webdriver.common.by import By


class DragdropPageLocators:
    IMAGE = (By.XPATH, "//div[@id='image']")
    DROPBOX = (By.XPATH, "//div[@id='box']")
    DROPBOX_TEXT = (By.XPATH, "//div[@id='box']/p")


