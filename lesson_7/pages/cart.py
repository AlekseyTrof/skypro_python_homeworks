from selenium.webdriver.common.by import By


class Cart:

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    def put_firt_name(self, first_name):
        self.driver.find_element(
            By.CSS_SELECTOR, '#first-name').send_keys(first_name)

    def put_last_name(self, last_name):
        self.driver.find_element(
            By.CSS_SELECTOR, '#last-name').send_keys(last_name)

    def put_zip(self, zip):
        self.driver.find_element(
            By.CSS_SELECTOR, '#postal-code').send_keys(zip)

    def click_continue(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '#continue').click()

    def quit(self):
        self.driver.quit()
