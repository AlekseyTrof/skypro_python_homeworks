from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")
driver.implicitly_wait(16)
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

txt = driver.find_element(By.CSS_SELECTOR, ".bg-success")
print(txt.text)

driver.quit()
