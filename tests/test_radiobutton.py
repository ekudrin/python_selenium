import allure

from pages.radiobutton_page import RadioButtonPage


@allure.feature("RadioButton")
class TestRadioButton:

    @allure.title("Check radiobutton list")
    def test_radiobutton(self, driver):
        radiobutton_page = RadioButtonPage(driver, "https://formy-project.herokuapp.com/radiobutton")
        radiobutton_page.open()
        button_list, selected_element = radiobutton_page.select_random_button()
        radiobutton_page.check_selected_radiobutton(button_list, selected_element)
