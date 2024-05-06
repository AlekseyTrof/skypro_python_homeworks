from selenium.webdriver.common.by import By


class Registration:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def open(self, browser):
        self.driver.get(browser)

    def put_username(self, username):
        self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="username"]').send_keys(username)

    def put_password(self, password):
        self.driver.find_element(
            By.CSS_SELECTOR, '#password').send_keys(password)

    def click_login(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="login-button"]').click()

    def quit(self):
        self.driver.quit()