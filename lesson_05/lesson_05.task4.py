from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

username = 'input#username'
password = 'input#password'
login =  'i.fa'
code = 'div#flash'
search_input = driver.find_element(By.CSS_SELECTOR, username)
search_input.send_keys("tomsmith")
sleep(3)
search_input = driver.find_element(By.CSS_SELECTOR, password)
search_input.send_keys("SuperSecretPassword!")
sleep(3)
search_input = driver.find_element(By.CSS_SELECTOR, login).click()

code_phrase = driver.find_element(By.CSS_SELECTOR, code).text

print(code_phrase)


sleep(3)

driver.quit()