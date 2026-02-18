from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from Pages.SingInPage import ShopSingIn
from Pages.MainPage import MainPage
from Pages.CartPage import CartPage
from Pages.FormPage import FormPage

def test_shopping():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    login_page = ShopSingIn(browser)
    main_page = MainPage(browser)
    cart_page = CartPage(browser)
    form_page = FormPage(browser)
    login_page.authorization()
    main_page.orders()
    cart_page.checkout()
    form_page.fill_form()

    total_text = form_page.get_text()
    result = total_text.split("$")[1]  
    assert result == "58.29"

    browser.quit()