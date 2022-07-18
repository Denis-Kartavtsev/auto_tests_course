from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Bob")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Billi')
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('bob@mail.ru')
    
# используем путь до директории исполн¤ймого файла, прописываем какой файл прикложить(должен лежать в одной папке с исполн¤ймым файлом, иначе прописывать ..../путь

    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'file_test.txt')
    input_element = browser.find_element(By.ID, 'file')
    input_element.send_keys(file_path)
    
# выбор элемента, скролл до него     
    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()
