import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from Pages.SingInPage import ShopSingIn
from Pages.MainPage import MainPage
from Pages.CartPage import CartPage
from Pages.FormPage import FormPage


@allure.title("Проверка оформления заказа в интернет-магазине")
@allure.description("Тест проверяет успешное оформление заказа и корректность итоговой суммы.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping() -> None:
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    with allure.step("Открыть страницу авторизации"):
        login_page = ShopSingIn(browser)

    main_page = MainPage(browser)
    cart_page = CartPage(browser)
    form_page = FormPage(browser)

    with allure.step("Авторизоваться в системе"):
        login_page.authorization()

    with allure.step("Добавить товары в корзину"):
        main_page.orders()

    with allure.step("Перейти к оформлению заказа"):
        cart_page.checkout()

    with allure.step("Заполнить форму заказа"):
        form_page.fill_form()

    with allure.step("Получить итоговую сумму заказа"):
        total_text = form_page.get_text()
        result = total_text.split("$")[1]

    with allure.step("Проверить, что итоговая сумма равна 58.29"):
        assert result == "58.29"

    browser.quit()
