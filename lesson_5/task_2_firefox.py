from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

for x in range(3):
    driver = webdriver.Firefox()

    driver.get("http://uitestingplayground.com/dynamicid")

    click = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    click.click()

    sleep(2)  # успеть посмотреть что произошло в браузере
    driver.quit()

