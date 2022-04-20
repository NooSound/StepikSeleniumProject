import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time





def pytest_addoption(parser):
    parser.addoption('--language', action='store', default= 'eb-gb',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    #указываем язык браузера с помощью WebDriver
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    yield browser
    time.sleep(2)  #визуальная проверка изменения языка
    print("\nquit browser..")
    browser.quit()