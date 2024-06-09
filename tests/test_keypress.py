import allure

from pages.keypress_page import KeyPressPage


@allure.feature("Key Press")
class KeyPress:
    @allure.title("Check input")
    def test_keypress(self,driver):
        keypress_page = KeyPressPage(driver, 'https://formy-project.herokuapp.com/keypress')
        keypress_page.open()
        text = keypress_page.fill_input()
        keypress_page.check_input_text(text)
