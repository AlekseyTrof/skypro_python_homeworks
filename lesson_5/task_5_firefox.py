from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(1)

field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
field.send_keys("1000")
sleep(1)

field.clear()
sleep(1)

field.send_keys("999")
sleep(1)

driver.quit()
