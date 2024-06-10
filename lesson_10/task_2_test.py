from pages.calculator import Calculator
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import allure

@allure.title("Тестирование калькулятора")
@allure.description("Проверка корректности работы калькулятора")
@allure.feature("Калькулятор")
@allure.severity("Critical")
def test_calculator():
    """
    Проверить корректность работы калькулятора
    """
    with allure.step("Подключиться к драйверу"):
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()))
        calculator = Calculator(driver)
    with allure.step("Очистить окно с таймером ожидания калькулятора"):
        calculator.clear_waits()
    with allure.step("Ввести число ожидания в секундах"):
        calculator.put_new_waits(45)
    with allure.step("Кликнуть на цифру 7"):
        calculator.click_7()
    with allure.step("Кликнуть на знак +"):
        calculator.click_plus()
    with allure.step("Кликнуть на цифру 8"):
        calculator.click_8()
    with allure.step("Кликнуть на знак ="):
        calculator.click_equals()
    with allure.step("Дождаться, когда в окне ответа не появится ответ"):
        calculator.wait_time(driver, "15")  # следует изменить время ожидания в классе, если время в put_new_waits() изменилось
    with allure.step("Считать результат из поля"):
        answer = calculator.watch_answer()
    with allure.step("Сравнить ответ с результатом"):
        assert answer == "15"  # следует изменить ответ, если в calculator.wait_time(driver, "15") - ответ другой
    with allure.step("Закрыть браузер"):
        calculator.quit()
