from pages.keypress_page import KeyPressPage


def test_keypress(driver):
    keypress_page = KeyPressPage(driver, 'https://formy-project.herokuapp.com/keypress')
    keypress_page.open()
    text = keypress_page.fill_input()
    keypress_page.check_input_text(text)
