from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.maximize_window()


element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.ID, "landscape"))
)

div = driver.find_element(By.ID, "image-container")
images = div.find_elements(By.TAG_NAME, "img")
third_img = images[2]
print(third_img.get_dom_attribute("src"))