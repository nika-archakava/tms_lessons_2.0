import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def click(driver, xpath_value):
    xpath = (By.XPATH, xpath_value)
    wait = WebDriverWait(driver, 10)
    for condition in [
        EC.presence_of_element_located,
        EC.visibility_of_element_located,
        EC.element_to_be_clickable,
    ]:
        wait.until(condition(xpath))
    element = driver.find_element(*xpath)
    element.click()


class TestClass:
    def test_selenium_first(self, driver):
        driver.get("https://www.thesaurus.com/")
        click(driver, "//*[@id = 'onetrust-accept-btn-handler']")
        input_string = driver.find_element(By.XPATH, "//input[@id='global-search']")
        input_string.send_keys("love")
        click(driver, "//*[@class = 'SFL_CJwX_oOmq1DF63xo']")
        sixth_synonym = driver.find_element(By.XPATH, "(//*[@data-linkid='y2woe7'])[6]")
        print_sixth_synonym = sixth_synonym.text

        print(f'\n\nThe sixth synonym of the word Love is {print_sixth_synonym}')
        all_synonyms = driver.find_elements(By.XPATH, "(//*[@data-linkid='y2woe7'])")
        print(f'\nWord "Love" has {len(all_synonyms)} synonyms.All synonyms are listed below.')
        x = 0
        for i in all_synonyms:
            x += 1
            print(f'\n{x} - {i.text}')
