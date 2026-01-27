def test_shopping():
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    username = driver.find_element(By.CSS_SELECTOR, 'input#user-name')
    username.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR, 'input#password')
    password.send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()

    driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()
    driver.find_element(By.CSS_SELECTOR, 'button#checkout').click()

    firstname = driver.find_element(By.CSS_SELECTOR, 'input#first-name')
    firstname.send_keys("Vlad")
    lastname = driver.find_element(By.CSS_SELECTOR, 'input#last-name')
    lastname.send_keys("Buchko")
    postcode = driver.find_element(By.CSS_SELECTOR, 'input#postal-code')
    postcode.send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, 'input#continue').click()

    assert WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[data-test="total-label"]'), "58.29")
        )
    
    driver.quit()