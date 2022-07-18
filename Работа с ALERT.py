from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *
import time

link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return log(abs(12*sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.XPATH, '//button[@type = "submit"]')
    button1.click()

    # работа с окошком alert
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    x = str(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(x)
    button2 = browser.find_element(By.XPATH, '//button')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()




