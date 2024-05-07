from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def put_fn(self, first_name):
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(first_name)

    def put_ln(self, last_name):
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)

    def put_address(self, address):
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)

    def put_email(self, email):
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)

    def put_pn(self, phone_number):
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone_number)

    def put_zc(self, zip_code):
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys(zip_code)

    def clear_zc(self):
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="zip-code"]').clear

    def put_city(self, city):
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)

    def put_country(self, country):
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)

    def put_job(self, job_position):
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="job-position"]'
            ).send_keys(job_position)

    def put_company(self, company):
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)

    def click_submit(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']").click()

    def flied_zip_code(self):
        zip_code_field = self.driver.find_element(
            By.CSS_SELECTOR, '#zip-code').value_of_css_property(
                "background-color")
        return zip_code_field

    def flied_green(self, field):
        field_color = self.driver.find_element(
                By.CSS_SELECTOR, field).value_of_css_property('background-color')
        return field_color

    def quit(self):
        self.driver.quit()
