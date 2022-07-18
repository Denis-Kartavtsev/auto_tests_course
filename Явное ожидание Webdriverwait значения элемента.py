from selenium import webdriver
from selenium.webdriver.common.by import By
# подключение библиотеки с методами условий ожидания
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from math import *
import time


def calc(x):
    return log(abs(12 * sin(x)))


link = 'http://suninjuly.github.io/explicit_wait2.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)
    # проверяем нужный нам текст($100) в интересуещем нас элементе в течении 13 секунд
    text_element = WebDriverWait(browser, 13).until(Ec.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element(By.ID, 'book')
    button.click()
    input1 = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    x_element = browser.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    x = calc(x)
    y = str(x)
    input1.send_keys(y)
    button2 = browser.find_element(By.ID, 'solve')
    button2.click()


finally:
    time.sleep(16)
    browser.quit()
