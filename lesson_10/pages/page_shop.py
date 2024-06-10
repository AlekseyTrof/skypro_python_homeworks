from selenium.webdriver.common.by import By


class PageShop:
    """
        Страница для выбора товаров для покупки в магазине
    """
    def __init__(self, driver):
        self.driver = driver

    def add_backpack(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()

    def add_bolt_t_shirt(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()

    def add_onesie(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def get_cart(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '.shopping_cart_link').click()

    def quit(self) -> None:
        self.driver.quit()
