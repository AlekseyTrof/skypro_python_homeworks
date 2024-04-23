from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

for x in range(3):
    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.get("http://uitestingplayground.com/classattr")

    click = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    click.send_keys(Keys.RETURN)
    sleep(1)
    driver.switch_to.alert.accept()  # Принять предупреждение

    sleep(1)
    driver.quit()
