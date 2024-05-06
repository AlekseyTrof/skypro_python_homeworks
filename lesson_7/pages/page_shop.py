from selenium.webdriver.common.by import By


class PageShop:

    def __init__(self, driver):
        self.driver = driver

    def add_backpack(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()

    def add_bolt_t_shirt(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()

    def add_onesie(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def get_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '.shopping_cart_link').click()

    def quit(self):
        self.driver.quit()
