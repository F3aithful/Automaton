from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")
driver.maximize_window()

button = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
button.click()

driver.implicitly_wait(16)
text = driver.find_element(By.CSS_SELECTOR, 'p[class="bg-success"]').text

print(text)

driver.quit()
