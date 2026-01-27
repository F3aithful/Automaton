from filling_form import FormFill

filling_form = FormFill()

def test_fill_form():
    from selenium import webdriver
    from selenium.webdriver.edge.service import Service as EdgeService
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    driver = webdriver.Edge(service=EdgeService(r"C:\Users\ebnym\.wdm\drivers\edgedriver\win64\144.0.3719.92\msedgedriver.exe"))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

    filling_form.fill_input(driver,"input[name='first-name']", "Иван")
    filling_form.fill_input(driver,"input[name='last-name']", "Петров")
    filling_form.fill_input(driver,"input[name='address']", "Ленина, 55-3")
    filling_form.fill_input(driver,"input[name='e-mail']", "test@skypro.com")
    filling_form.fill_input(driver,"input[name='phone']", "+7985899998787")
    filling_form.fill_input(driver,"input[name='zip-code']", "")
    filling_form.fill_input(driver,"input[name='city']", "Москва")
    filling_form.fill_input(driver,"input[name='country']", "Россия")
    filling_form.fill_input(driver,"input[name='job-position']", "QA")
    filling_form.fill_input(driver,"input[name='company']", "SkyPro")
    
    submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    submit.click()

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert")))

    success_alerts = driver.find_elements(By.CSS_SELECTOR, "div.alert-success")
    danger_alerts = driver.find_elements(By.CSS_SELECTOR, "div.alert-danger")

    assert len(danger_alerts) == 1
    assert len(success_alerts) == 9

    driver.quit()