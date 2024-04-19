from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")
sleep(1)

username = driver.find_element(By.CSS_SELECTOR, '#username')
username.send_keys("tomsmith")
sleep(1)

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys("SuperSecretPassword!")
sleep(1)

driver.find_element(By.CSS_SELECTOR, '.radius').click

sleep(1)
driver.quit()