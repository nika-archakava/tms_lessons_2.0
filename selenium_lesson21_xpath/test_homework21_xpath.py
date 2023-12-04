import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestClass:
    def test_selenium_first(self, driver):
        driver.get("https://www.thesaurus.com/")
        accept_cookies_button = driver.find_element(By.XPATH, "//*[@id = 'onetrust-accept-btn-handler']")
        accept_cookies_button.click()
        input_string = driver.find_element(By.XPATH, "//input[@id='global-search']")
        input_string.send_keys("love")
        submit_button = driver.find_element(By.XPATH, "//*[@class = 'SFL_CJwX_oOmq1DF63xo']")
        submit_button.click()
        sixth_synonym = driver.find_element(By.XPATH, "(//*[@data-linkid='y2woe7'])[6]")
        print_sixth_synonym = sixth_synonym.text

        print(f'\n\nThe sixth synonym of the word Love is {print_sixth_synonym}')
        all_synonyms = driver.find_elements(By.XPATH, "(//*[@data-linkid='y2woe7'])")
        print(f'\nWord "Love" has {len(all_synonyms)} synonyms.All synonyms are listed below.')
        x = 0
        for i in all_synonyms:
            x += 1
            print(f'\n{x} - {i.text}')
