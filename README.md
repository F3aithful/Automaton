# Automaton

## Описание проекта

Проект содержит автоматизированные UI-тесты, написанные с использованием
Selenium и Pytest.

В проекте реализованы: - Тест медленного калькулятора - Тест оформления
заказа в интернет-магазине

Для формирования отчетности используется Allure.

------------------------------------------------------------------------

## Используемые технологии

-   Python
-   Pytest
-   Selenium
-   WebDriver Manager
-   Allure

------------------------------------------------------------------------

## Установка и подготовка проекта

1.  Установить зависимости:

Пользователи macOS: запустите в терминале VS Code команду

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Пользователи Windows: запустите в терминале VS Code команду

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

scoop install allure

pip install pytest

pip install allure-pytest

pip install webdriver-manager

pip install selenium

------------------------------------------------------------------------

## Запуск тестов с формированием результатов

Для запуска тестов с сохранением результатов Allure:

pytest --alluredir allure-result

После выполнения тестов будет создана папка:

allure-results

------------------------------------------------------------------------

## Формирование отчета Allure

Для генерации отчета выполнить:

allure serve allure-results

После генерации будет создана папка:

allure-report

------------------------------------------------------------------------

## Просмотр сформированного отчета

Если использовалась команда:

allure serve allure-results

Отчет откроется автоматически в браузере.

------------------------------------------------------------------------

## Важно

Папки allure-results и allure-report в репозиторий не добавляются.
