from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'for_lesson_2_2_step_8.txt')  # добавляем к этому пути имя файла

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Firstname")
    browser.find_element(By.NAME, "lastname").send_keys("Lastname")
    browser.find_element(By.NAME, "email").send_keys("e@ma.il")
    browser.find_element(By.NAME, "file").send_keys(file_path)
    browser.find_element(By.TAG_NAME, 'button').click()


finally:
    time.sleep(5)
    browser.quit()
