from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self, driver):
        self.driver = driver

    def watch_total(self):
        total = self.driver.find_element(
            By.CSS_SELECTOR, '.summary_total_label').text
        return total

    def quit(self):
        self.driver.quit()
