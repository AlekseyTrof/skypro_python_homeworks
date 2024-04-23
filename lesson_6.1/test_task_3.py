from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

def test_saucedeme():
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(4)
    driver.maximize_window()

    # Логинимся как пользователь standard_user
    user_log = driver.find_element(By.CSS_SELECTOR, '[data-test="username"]')
    user_log.send_keys("standard_user")
    pass_log = driver.find_element(By.CSS_SELECTOR, '#password')
    pass_log.send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()

    # Добавляем товары в корзину
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    # Переходим в корзину
    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

    # Проходим оформление заказа
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    # Заполняем данные и оформляем заказ
    f_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
    f_name.send_keys("Alex")
    l_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
    l_name.send_keys("Trofimov")
    l_name = driver.find_element(By.CSS_SELECTOR, '#postal-code')
    l_name.send_keys("153000")
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    # Получаем и проверяем итоговую стоимость
    total = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    assert total == "Total: $58.29"

    driver.quit()
