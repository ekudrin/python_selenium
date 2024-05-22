from pages.dragdrop_page import DragdropPage


def test_drag_and_drop(driver):
    dragdroppage = DragdropPage(driver, 'https://formy-project.herokuapp.com/dragdrop')
    dragdroppage.open()
    dragdroppage.dragndropimage()
    dragdroppage.check_dropbox_text()

