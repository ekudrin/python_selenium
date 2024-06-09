import allure

from pages.fileupload_page import FileUploadPage


@allure.feature("File Upload")
class TestFileUpload:
    @allure.title("Check file upload")
    def test_upload_file(self,driver):
        file_upload_page = FileUploadPage(driver, 'https://formy-project.herokuapp.com/fileupload')
        file_upload_page.open()
        file_name, text = file_upload_page.upload_file()
        file_upload_page.check_input_text(file_name, text)


    @allure.title("Check Reset button")
    def test_reset_upload(self,driver):
        file_upload_page = FileUploadPage(driver, 'https://formy-project.herokuapp.com/fileupload')
        file_upload_page.open()
        text = file_upload_page.reset_upload()
        file_upload_page.check_default_input_text(text)
