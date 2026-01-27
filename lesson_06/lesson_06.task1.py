from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")
driver.maximize_window()

button = driver.find_element(By.CSS_SELECTOR, 'button#ajaxButton')
button.click()

waiter = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )
text = driver.find_element(By.CSS_SELECTOR, 'p[class="bg-success"]').text

print(text)

driver.quit()
