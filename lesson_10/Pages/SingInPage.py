from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ShopSingIn:
    """Класс страницы авторизации магазина."""

    def __init__(self, browser: WebDriver) -> None:
        """
        Инициализация страницы авторизации.

        :param browser: Экземпляр WebDriver
        :return: None
        """
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def authorization(self) -> None:
        """
        Выполняет авторизацию пользователя.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys("standard_user")
        self._driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys("secret_sauce")
        self._driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()