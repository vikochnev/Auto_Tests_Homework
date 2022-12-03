import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(number):
    return math.log(abs(12 * math.sin(int(number))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(4)

    button = WebDriverWait(browser, 60).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    output_alert = browser.switch_to.alert
    output = output_alert.text.split(': ')[-1]
    print(f'Answer is:\n {output}')
    output_alert.accept()

finally:
    browser.quit()
