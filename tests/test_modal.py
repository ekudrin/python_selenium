from pages.modal_page import ModalPage


def test_modal_text(driver):
    modal_page = ModalPage(driver, 'https://formy-project.herokuapp.com/modal')
    modal_page.open()
    modal_page.check_text_in_modal()


def test_close_modal(driver):
    modal_page = ModalPage(driver, 'https://formy-project.herokuapp.com/modal')
    modal_page.open()
    modal_page.check_close_button()
