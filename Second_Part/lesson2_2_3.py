import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()
try:
    link = browser.get('http://suninjuly.github.io/selects1.html')
    time.sleep(2)

    number1 = browser.find_element_by_id('num1')
    number1_value = int(number1.text)
    print(number1_value)

    number2 = browser.find_element_by_id('num2')
    number2_value = int(number2.text)
    print(number2_value)

    total_value = int(number1_value) + int(number2_value)
    print(total_value)

    b5 = Select(browser.find_element_by_id('dropdown'))
    b5.select_by_visible_text(str(total_value))

    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()
