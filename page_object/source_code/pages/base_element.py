from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver, xpath):
        self.driver = driver
        self.xpath = xpath

    def hover(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.xpath)
        actions.move_to_element(element).perform()

    def assert_element(self, clickable=False, return_many=False):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.xpath)))
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath)))

        if clickable:
            wait.until(EC.element_to_be_clickable((By.XPATH, self.xpath)))

        if return_many:
            result = self.driver.find_elements(By.XPATH, self.xpath)
        else:
            result = self.driver.find_element(By.XPATH, self.xpath)

        return result

    def custom_click(self):
        element = self.assert_element(clickable=True)
        element.click()
