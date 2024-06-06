from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    """
        Методы работы с калькулятором на сайте
    """

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def clear_waits(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()

    def put_new_waits(self, wait : int) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(wait)

    def click_7(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()

    def click_plus(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, "span.operator:nth-child(4)").click()

    def click_8(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, "span.btn:nth-child(2)").click()

    def click_equals(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, "span.btn:nth-child(15)").click()

    # Так же можно дописать остальные цифры при необходимости

    def wait_time(celf, driver, answer : str) -> None:
        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), answer)
            )

    def watch_answer(self) -> str:
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result

    def quit(self) -> None:
        self.driver.quit()
