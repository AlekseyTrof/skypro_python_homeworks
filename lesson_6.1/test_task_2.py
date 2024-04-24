from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
    )


def test_calculator():
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    browser.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()
    browser.find_element(By.CSS_SELECTOR, "span.operator:nth-child(4)").click()
    browser.find_element(By.CSS_SELECTOR, "span.btn:nth-child(2)").click()
    browser.find_element(By.CSS_SELECTOR, "span.btn:nth-child(15)").click()

    WebDriverWait(browser, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    result = browser.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15"

    browser.quit()
