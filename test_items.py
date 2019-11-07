link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_basket_button(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert len(button) == 1, 'Кнопка не найдена'
