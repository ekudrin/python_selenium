import allure

from pages.dragdrop_page import DragdropPage


@allure.feature("Drag and Drop")
class TestDragDrop:
    @allure.title("Check drag n drop page")
    def test_drag_and_drop(self, driver):
        drag_n_drop_page = DragdropPage(driver, 'https://formy-project.herokuapp.com/dragdrop')
        drag_n_drop_page.open()
        drag_n_drop_page.drag_n_drop_image()
        drag_n_drop_page.check_dropbox_text()
