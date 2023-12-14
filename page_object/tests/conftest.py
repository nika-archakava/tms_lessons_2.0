import pytest
from selenium import webdriver

from page_object.source_code.pages.main.main_page import MainPage


@pytest.fixture
def driver():
    with webdriver.Chrome() as driver:
        yield driver


@pytest.fixture(autouse=True)
def open_main_page(driver):
    main_page = MainPage(driver)
    main_page.driver.get('https://myfin.by/')
