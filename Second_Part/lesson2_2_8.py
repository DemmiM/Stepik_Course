import os
import time
from selenium import webdriver


browser = webdriver.Chrome()

try:
    website = browser.get('http://suninjuly.github.io/file_input.html')

    fist_name = browser.find_element_by_css_selector('input[name="firstname"]')
    fist_name.send_keys("Maxim")
    last_name = browser.find_element_by_css_selector('input[name="lastname"]')
    last_name.send_keys('Minin')
    email = browser.find_element_by_css_selector('input[name="email"]')
    email.send_keys('maxim@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'selen.txt')           # добавляем к этому пути имя файла

    uploading_button = browser.find_element_by_id('file')
    uploading_button.send_keys(file_path)

    browser.find_element_by_css_selector('button.btn').click()


finally:
    time.sleep(10)
    browser.quit()
