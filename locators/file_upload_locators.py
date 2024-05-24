from selenium.webdriver.common.by import By


class FileUploadPageLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, "#file-upload-field")
    RESET_BUTTON = (By.XPATH, "//button[text()='Reset']")

