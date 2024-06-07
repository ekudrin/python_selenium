from pages.page_scroll_page import PageScrollPage


def test_scroll_to_fields(driver):
    scroll_page = PageScrollPage(driver, 'https://formy-project.herokuapp.com/scroll')
    scroll_page.open()
    full_name_text, date_text = scroll_page.fill_text_fields()
    scroll_page.check_fields(full_name_text, date_text)


