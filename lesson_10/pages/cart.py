from selenium.webdriver.common.by import By


class Cart:
    """
        Страница для ввода информации о покупателя и номера карты
    """
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    def put_firt_name(self, first_name : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#first-name').send_keys(first_name)

    def put_last_name(self, last_name : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#last-name').send_keys(last_name)

    def put_zip(self, zip : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#postal-code').send_keys(zip)

    def click_continue(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#continue').click()

    def quit(self) -> None:
        self.driver.quit()
