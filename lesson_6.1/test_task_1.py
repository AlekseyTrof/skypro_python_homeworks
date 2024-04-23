from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(4)
browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = "Иван"
last_name = "Петров"
address = "Ленина, 55-3"
email = "test@skypro.com"
phone_number = "+7985899998787"
zip_code = ""
city = "Москва"
country = "Россия"
job_position = "QA"
company = "SkyPro"

browser.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(first_name)
browser.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)
browser.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)
browser.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)
browser.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone_number)
browser.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys(zip_code)
browser.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
browser.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)
browser.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(job_position)
browser.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)

browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Проверка подсветки полей
zip_code_field = browser.find_element(By.CSS_SELECTOR, '#zip-code')
assert "rgba(248, 215, 218, 1)" == zip_code_field.value_of_css_property("background-color")

highlighted_fields = browser.find_elements(By.CSS_SELECTOR, 'div.alert.py-2.alert-success')
for field in highlighted_fields:
    assert "rgba(209, 231, 221, 1)" == field.value_of_css_property("background-color")
     
browser.quit()
