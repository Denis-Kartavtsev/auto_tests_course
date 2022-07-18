from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *
import time


def calc(x):
    return log(abs(12 * sin(x)))


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
    # орпеделяем новое окно, на которое будем переходить
    new_window = browser.window_handles[1]
    # переключить на окно(имя окна)
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    y = str(calc(x))
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    button2 = browser.find_element(By.XPATH, '//button')
    button2.click()

finally:
    time.sleep(5)
    browser.quit()




