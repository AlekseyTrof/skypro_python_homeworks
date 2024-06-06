from selenium.webdriver.common.by import By


class Registration:
    """
        Страница для регистрации на сайте
    """

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def open(self, browser : str) -> None:
        self.driver.get(browser)

    def put_username(self, username : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="username"]').send_keys(username)

    def put_password(self, password : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#password').send_keys(password)

    def click_login(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="login-button"]').click()

    def quit(self) -> None:
        self.driver.quit()