from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value')
    print(x_element)
    x = x_element.text
    print(x)
    y = calc(x)

    browser.find_element_by_css_selector('#answer').send_keys(y)
    browser.find_element_by_css_selector("[for=robotCheckbox]").click()
    browser.find_element_by_css_selector("[for=robotsRule]").click()
    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()
