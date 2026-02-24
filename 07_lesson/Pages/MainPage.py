from selenium.webdriver.common.by import By
class MainPage:

    def __init__(self, browser):
        self._driver = browser

    def orders(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-onesie').click()
        self._driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()