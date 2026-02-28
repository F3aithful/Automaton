from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalcPage:
    """Класс страницы медленного калькулятора."""

    def __init__(self, browser: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        :param browser: Экземпляр WebDriver
        :return: None
        """
        self._driver = browser
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def answer_delay(self) -> None:
        """
        Устанавливает задержку вычисления.

        :return: None
        """
        delay = self._driver.find_element(By.CSS_SELECTOR, 'input#delay')
        delay.clear()
        delay.send_keys("45")

    def nums(self) -> None:
        """
        Вводит выражение 7 + 8.

        :return: None
        """
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()

    def solution(self) -> None:
        """
        Нажимает кнопку вычисления результата.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, 'span.btn.btn-outline-warning').click()

    def waiting(self) -> str:
        """
        Ожидает появления результата вычисления.

        :return: Строковое значение результата
        """
        WebDriverWait(self._driver, 45).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
        )
        return self._driver.find_element(By.CSS_SELECTOR, "div.screen").text