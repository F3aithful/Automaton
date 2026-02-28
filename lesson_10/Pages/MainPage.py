from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    """Класс главной страницы магазина."""

    def __init__(self, browser: WebDriver) -> None:
        """
        Инициализация главной страницы.

        :param browser: Экземпляр WebDriver
        :return: None
        """
        self._driver = browser

    def orders(self) -> None:
        """
        Добавляет товары в корзину и переходит в корзину.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-onesie').click()
        self._driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()