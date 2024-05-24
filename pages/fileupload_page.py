import os

from generator.generator import generated_file
from locators.file_upload_locators import FileUploadPageLocators
from pages.base_page import BasePage


class FileUploadPage(BasePage):
    locators = FileUploadPageLocators()

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_visible(self.locators.UPLOAD_FILE).get_attribute('value')
        return file_name,text

    def reset_upload(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.RESET_BUTTON).click()
        return self.element_is_present(self.locators.UPLOAD_FILE).get_attribute('placeholder')

    def check_input_text(self,file_name,text):
        assert file_name == text, 'Input text does not match file name'

    def check_default_input_text(self, text):
        assert text == 'Choose a file...', "Input text does not match default message"
