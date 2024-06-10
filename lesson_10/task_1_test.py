from pages.bonigarcia import MainPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure

@allure.title("Тестирование полей на изменение цвета")
@allure.description("Если поле не заполенно, то оно отмечается красным цветом")
@allure.feature("Тестирование полей")
@allure.severity("Critical")
def test_bonig():
    """
    Проверка элементов при заполнении формы. 
    Когда все поля заполнены, тогда поле загорится зеленым,
    А если поле не полоднено, то красным
    """
    with allure.step("Подключиться к браузеру через драйвер"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        main_page = MainPage(driver)
    main_page.put_fn("Иван")
    main_page.put_ln("Петров")
    main_page.put_address("Ленина, 55-3")
    main_page.put_email("test@skypro.com")
    main_page.put_pn("+7985899998787")
    main_page.clear_zc()
    main_page.put_city("Москва")
    main_page.put_country("Россия")
    main_page.put_job("QA")
    main_page.put_company("SkyPro")
    main_page.click_submit()

    to_is_red = "rgba(248, 215, 218, 1)"
    with allure.step("Найти цвет поля через DevTools"):
        to_be_red = main_page.flied_zip_code()
    with allure.step("Проверить, что элемент красный, т.к. это поле не заполнено"):    
        assert to_is_red == to_be_red

    other_fields = ['#first-name', '#last-name', '#address', 
                '#city', '#country', '#e-mail', '#phone', '#job-position', '#company']
    with allure.step("Проверка остальных полей, что они зеленые"):
        for field in other_fields:
            field_color = main_page.flied_green(field)
            assert field_color == 'rgba(209, 231, 221, 1)'
    with allure.step("Закрыть браузер"):
        main_page.quit()
