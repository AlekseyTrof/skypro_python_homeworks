from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
skypro = WebDriverWait(driver, 20)

skypro.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.lead#text"), 'Done'))

loc = driver.find_element(By.CSS_SELECTOR, 'img#award')
print(loc.get_attribute("src"))

driver.quit()
