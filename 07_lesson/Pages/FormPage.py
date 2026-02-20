from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class FormPage:

    def __init__(self, browser):
        self._driver = browser

    def fill_form(self):
        self._driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys("Vlad")
        self._driver.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys("Buchko")
        self._driver.find_element(By.CSS_SELECTOR, 'input#postal-code').send_keys("123456")
        self._driver.find_element(By.CSS_SELECTOR, 'input#continue').click()

    def get_text(self):
        WebDriverWait(self._driver, 5).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test="total-label"]')) 
            ) 
        return self._driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]').text