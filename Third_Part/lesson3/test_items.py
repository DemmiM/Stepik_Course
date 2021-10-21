import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_btn(browser):
    browser.get(link)
    time.sleep(30)
    btn = browser.find_element_by_css_selector(".add-to-basket button.btn-add-to-basket")
    assert btn is not None, "Button is not exist"
