from pages.radiobutton_page import RadioButtonPage


def test_radiobutton(driver):
    radiobutton_page = RadioButtonPage(driver, "https://formy-project.herokuapp.com/radiobutton")
    radiobutton_page.open()
    button_list, selected_element = radiobutton_page.select_random_button()
    radiobutton_page.check_selected_checkbox(button_list, selected_element)
