from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Pages.CalcPage import CalcPage

def test_slow_calc():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calc_page = CalcPage(browser)
    calc_page.answer_delay()
    calc_page.nums()
    calc_page.solution()
    
    result = calc_page.waiting()
    assert result == "15"

    browser.quit()