from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *
import time


def calc(x):
    return log(abs(12 * sin(int(x))))


link = "http://suninjuly.github.io/math.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    # этих расчеты только в этой задаче, к автоматизации не относяться
    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")

    # вытянуть из выбранного элемента текст
    x = int(x_element.text)
    y = str(calc(x))
    input_x = browser.find_element(By.ID, "answer")
    input_x.send_keys(y)

    # установка чекбокса
    option1 = browser.find_element(By.CSS_SELECTOR, '[for = "robotCheckbox"]')
    option1.click()

    # поставить радиобаттон
    option2 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    option2.click()
    button = browser.find_element(By.XPATH, '//button ')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
