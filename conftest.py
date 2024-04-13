# написать тест для проверки наличия кнопки корзины с определенным текстом на различных языках
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")
    

from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")                 # использую данную фикстуру для импортирования в тестовый файл языка страницы
def language_name(request):
    return request.config.getoption("language")






