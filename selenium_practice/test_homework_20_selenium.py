import pytest
from datetime import datetime

from selenium import webdriver


class TestSelenium:
    @pytest.mark.parametrize("url, page_title", [["https://www.amazon.com/", "Amazon"],
                                                 ["https://www.apple.com/", "Apple"],
                                                 ["https://www.google.com/", "Google"]])
    def test_selenium_first_site(self, driver_chrome, driver_firefox, url, page_title):
        if page_title == "Google":
            driver = driver_chrome
        else:
            driver = driver_firefox
        driver.get(url)
        driver.save_screenshot(f'{page_title}_{int(datetime.now().timestamp())}.png')
        actual_page_title = driver.title
        assert page_title in actual_page_title
