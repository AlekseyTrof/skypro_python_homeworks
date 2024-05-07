from pages.calculator import Calculator
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_calculator():

    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()))

    calculator = Calculator(driver)
    calculator.clear_waits()
    calculator.put_new_waits(45)
    calculator.click_7()
    calculator.click_plus()
    calculator.click_8()
    calculator.click_equals()
    calculator.wait_time(driver, "15")  # следует изменить время ожидания в классе, если время в put_new_waits() изменилось
    answer = calculator.watch_answer()

    assert answer == "15"  # следует изменить ответ, если в calculator.wait_time(driver, "15") - ответ другой

    calculator.quit()
