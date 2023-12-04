import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    with webdriver.Chrome() as driver:
        yield driver
