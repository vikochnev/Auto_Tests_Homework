import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(number):
    return math.log(abs(12 * math.sin(int(number))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()

    output_alert = browser.switch_to.alert
    output = output_alert.text.split(': ')[-1]
    print(f'Answer is:\n {output}')
    output_alert.accept()

finally:
    browser.quit()
