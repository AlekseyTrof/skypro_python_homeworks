from pages.registration import Registration
from pages.page_shop import PageShop
from pages.cart import Cart
from pages.checkout import Checkout
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_calculator():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
        )

    reg = Registration(driver)
    reg.open("https://www.saucedemo.com/")
    reg.put_username("standard_user")
    reg.put_password("secret_sauce")
    reg.click_login()

    page_shop = PageShop(driver)
    page_shop.add_backpack()
    page_shop.add_bolt_t_shirt()
    page_shop.add_onesie()
    page_shop.get_cart()

    cart = Cart(driver)
    cart.click_checkout()
    cart.put_firt_name("Alex")
    cart.put_last_name("Trofimov")
    cart.put_zip("153000")
    cart.click_continue()

    checkout = Checkout(driver)
    total = checkout.watch_total()
    to_is = ("Total: $58.29")
    assert total == to_is
