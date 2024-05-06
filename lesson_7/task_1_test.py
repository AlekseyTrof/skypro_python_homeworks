from pages.bonigarcia import MainPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_bonig():

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
    to_be_red = main_page.flied_zip_code()
    assert to_is_red == to_be_red

    to_is_green = "rgba(209, 231, 221, 1)"
    to_be_green = main_page.flied_green()
    for field in to_be_green:
        assert to_is_green == field.value_of_css_property("background-color")

    main_page.quit()
