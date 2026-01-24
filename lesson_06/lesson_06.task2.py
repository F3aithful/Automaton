from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")
driver.maximize_window()

field = driver.find_element(By.CSS_SELECTOR, 'input')
field.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, 'button#updatingButton')
button.click()
text = button.text

print(text)

driver.quit()