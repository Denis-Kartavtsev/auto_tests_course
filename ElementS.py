from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(какой локатор ищем, "им¤ локатора")
    for element in elements:
        element.send_keys("вводим значение")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипул¤ций
    browser.quit()
----------------------------------------------------------------------------------

# есть еще така¤ конструкци¤ дл¤ проверки кол-ва эелентов
# данный сайт не существует, этот код приведен только дл¤ примера
browser.get("https://fake-shop.com/book1.html")

# добавл¤ем товар в корзину
add_button = browser.find_element(By.CSS_SELECTOR, ".add")
add_button.click()

# открываем страницу второго товара
browser.get("https://fake-shop.com/book2.html")

# добавл¤ем товар в корзину
add_button = browser.find_element(By.CSS_SELECTOR, ".add")
add_button.click()

# тестовый сценарий
# открываем корзину
browser.get("https://fake-shop.com/basket.html")

# ищем все добавленные товары
goods = browser.find_elements(By.CSS_SELECTOR, ".good")

# провер¤ем, что количество товаров равно 2
assert len(goods) == 2
