from pages.fileupload_page import FileUploadPage


def test_upload_file(driver):
    file_upload_page = FileUploadPage(driver, 'https://formy-project.herokuapp.com/fileupload')
    file_upload_page.open()
    file_name, text = file_upload_page.upload_file()
    file_upload_page.check_input_text(file_name, text)


def test_reset_upload(driver):
    file_upload_page = FileUploadPage(driver, 'https://formy-project.herokuapp.com/fileupload')
    file_upload_page.open()
    text = file_upload_page.reset_upload()
    file_upload_page.check_default_input_text(text)
