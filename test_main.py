from selenium import webdriver


class TestSelenium:
    def test_selenium_first(self):
        driver = webdriver.Chrome()
        driver.get("https://www.python.org/")
        current_url = driver.current_url
        assert "python" in current_url
