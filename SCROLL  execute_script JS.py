from selenium import webdriver
from selenium.webdriver.common.by import By
# для инциализаци объекта
from selenium.webdriver.support.ui import Select
from math import *
import time


def calc(x):
    return log(abs(12 * sin(x)))


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    x = str(calc(x))
    x_input = browser.find_element(By.ID, 'answer')
    x_input.send_keys(x)

    # поиск эелемента до которого будет выполнен скролл
    button = browser.find_element(By.ID, 'robotsRule')
    # выполнение скрипта для скролла
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)

    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()
    option2 = browser.find_element(By.ID, 'robotsRule')
    option2.click()
    button2 = browser.find_element(By.TAG_NAME, 'button')
    button2.click()

finally:
    time.sleep(5)
    browser.quit()
