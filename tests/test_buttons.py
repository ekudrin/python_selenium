from pages.buttons_page import ButtonsPage


def test_clickable_buttons(driver):
    buttons_page = ButtonsPage(driver, 'https://formy-project.herokuapp.com/buttons')
    buttons_page.open()
    buttons_page.check_all_buttons_clickable()


def test_dropdown_items_present(driver):
    buttons_page = ButtonsPage(driver, 'https://formy-project.herokuapp.com/buttons')
    buttons_page.open()
    buttons_page.check_dropdown_items_are_present()









