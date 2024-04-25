from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")
skypro = WebDriverWait(driver, 3)

field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
field.send_keys("SkyPro")

sky = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
sky.click()

skypro.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro"))

print(sky.text)

driver.quit()
