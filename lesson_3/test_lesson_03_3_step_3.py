from selenium import webdriver
from selenium.webdriver.common.by import By

# import pytest


def test_proper():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "div.first_block input.first").send_keys("firstname")
    browser.find_element(By.CSS_SELECTOR, "div.first_block input.second").send_keys("lastname")
    browser.find_element(By.CSS_SELECTOR, "div.first_block input.third").send_keys("email")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    browser.quit()


def test_fails():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "div.first_block input.first").send_keys("firstname")
    browser.find_element(By.CSS_SELECTOR, "div.first_block input.second").send_keys("lastname")
    browser.find_element(By.CSS_SELECTOR, "div.first_block input.third").send_keys("email")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    browser.quit()
