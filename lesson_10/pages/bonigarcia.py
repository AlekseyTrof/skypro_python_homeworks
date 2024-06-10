from selenium.webdriver.common.by import By


class MainPage:
    """
        методы работы с формой Hands-On Selenium WebDriver with Java
        Заполнение всех полей и отправка формы
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def put_fn(self, first_name : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(first_name)

    def put_ln(self, last_name : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)

    def put_address(self, address : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)

    def put_email(self, email : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)

    def put_pn(self, phone_number : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone_number)

    def put_zc(self, zip_code : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys(zip_code)

    def clear_zc(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="zip-code"]').clear

    def put_city(self, city : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)

    def put_country(self, country : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)

    def put_job(self, job_position : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="job-position"]'
            ).send_keys(job_position)

    def put_company(self, company : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)

    def click_submit(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']").click()

    def flied_zip_code(self) -> str:
        zip_code_field = self.driver.find_element(
            By.CSS_SELECTOR, '#zip-code').value_of_css_property(
                "background-color")
        return zip_code_field

    def flied_green(self, field : str) -> str:
        field_color = self.driver.find_element(
                By.CSS_SELECTOR, field).value_of_css_property('background-color')
        return field_color

    def quit(self) -> None:
        self.driver.quit()
