import pytest
from selenium import webdriver


@pytest.fixture
def driver_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options)


@pytest.fixture
def driver_firefox():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    return webdriver.Firefox(options)
