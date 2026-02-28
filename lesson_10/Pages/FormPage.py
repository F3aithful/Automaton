from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class FormPage:
    """Класс страницы оформления заказа."""

    def __init__(self, browser: WebDriver) -> None:
        """
        Инициализация страницы формы заказа.

        :param browser: Экземпляр WebDriver
        :return: None
        """
        self._driver = browser

    def fill_form(self) -> None:
        """
        Заполняет форму оформления заказа.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys("Vlad")
        self._driver.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys("Buchko")
        self._driver.find_element(By.CSS_SELECTOR, 'input#postal-code').send_keys("123456")
        self._driver.find_element(By.CSS_SELECTOR, 'input#continue').click()

    def get_text(self) -> str:
        """
        Получает итоговую сумму заказа.

        :return: Строка с итоговой суммой
        """
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test="total-label"]'))
        )
        return self._driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]').text