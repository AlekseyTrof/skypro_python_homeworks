from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def test_form_elements():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(4)
    driver.maximize_window()

    first_name = "Иван"
    last_name = "Петров"
    address = "Ленина, 55-3"
    email = "test@skypro.com"
    phone_number = "+7985899998787"
    city = "Москва"
    country = "Россия"
    job_position = "QA"
    company = "SkyPro"

    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(first_name)
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone_number)
    driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(job_position)
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка подсветки полей
    zip_code_field = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property("background-color")
    assert "rgba(248, 215, 218, 1)" == zip_code_field

    highlighted_fields = driver.find_elements(By.CSS_SELECTOR, '.alert-success')
    for field in highlighted_fields:
        assert "rgba(209, 231, 221, 1)" == field.value_of_css_property("background-color")

    driver.quit()
