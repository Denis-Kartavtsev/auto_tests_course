from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# для инциализаци объекта работы со списком
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # для данной задачи необходим подсчет суммы на странице
    x_element = browser.find_element(By.XPATH, "//span[@id='num1']")
    x = int(x_element.text)
    y_element = browser.find_element(By.XPATH, "//span[@id='num2']")
    y = int(y_element.text)
    s = str(x + y)

    # поиск выбор значени из списка
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(s)   
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
