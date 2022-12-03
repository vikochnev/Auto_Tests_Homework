import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex")
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(y))
    browser.find_element(By.CSS_SELECTOR, ".check-input").click()

    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()



finally:
    time.sleep(5)
    browser.quit()
