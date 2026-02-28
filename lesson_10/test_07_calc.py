import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Pages.CalcPage import CalcPage


@allure.title("Проверка работы медленного калькулятора")
@allure.description("Тест проверяет корректность вычисления выражения 7 + 8 с задержкой ответа.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calc() -> None:
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Открыть страницу калькулятора"):
        calc_page = CalcPage(browser)

    with allure.step("Установить задержку вычисления"):
        calc_page.answer_delay()

    with allure.step("Ввести выражение 7 + 8"):
        calc_page.nums()

    with allure.step("Нажать кнопку равно"):
        calc_page.solution()

    with allure.step("Дождаться результата вычисления"):
        result = calc_page.waiting()

    with allure.step("Проверить, что результат равен 15"):
        assert result == "15"

    browser.quit()