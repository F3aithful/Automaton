from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс страницы корзины."""

    def __init__(self, browser: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        :param browser: Экземпляр WebDriver
        :return: None
        """
        self._driver = browser

    def checkout(self) -> None:
        """
        Переходит к оформлению заказа.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, 'button#checkout').click()