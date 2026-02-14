from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CalcPage:

    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def answer_delay(self):
        delay = self._driver.find_element(By.CSS_SELECTOR, 'input#delay')
        delay.clear()
        delay.send_keys("45")

    def nums(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()

    def solution(self):
        self._driver.find_element(By.CSS_SELECTOR, 'span.btn.btn-outline-warning').click()

    def waiting(self):
        assert WebDriverWait(self._driver, 45).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
            )
        return self._driver.find_element(By.CSS_SELECTOR, "div.screen").text