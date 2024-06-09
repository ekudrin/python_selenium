import allure

from pages.modal_page import ModalPage


@allure.feature("Modal")
class TestModal:
    @allure.title("Check modal text")
    def test_modal_text(self, driver):
        modal_page = ModalPage(driver, 'https://formy-project.herokuapp.com/modal')
        modal_page.open()
        modal_page.check_text_in_modal()

    @allure.title("Check modal close button")
    def test_close_modal(self, driver):
        modal_page = ModalPage(driver, 'https://formy-project.herokuapp.com/modal')
        modal_page.open()
        modal_page.check_close_button()
