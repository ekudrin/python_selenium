from selenium.webdriver.common.by import By


class ModalPageLocators:
    OPEN_BUTTON = (By.CSS_SELECTOR, "#modal-button")
    # modal window
    MODAL_WINDOW = (By.CSS_SELECTOR, "div[class='modal-content']")
    MODAL_TEXT = (By.CSS_SELECTOR, "div[class='modal-body']")
    OK_BUTTON = (By.CSS_SELECTOR, "#ok-button")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "#close-button")
