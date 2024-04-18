from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

click = driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
for x in range (5):
    sleep(1)
    click.click()


find_add = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
print("Найдено", len(find_add), "кнопок Delete")

sleep(2)  # успеть посмотреть что произошло в браузере
driver.quit()