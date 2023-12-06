import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    with webdriver.Chrome() as driver:
        yield driver


def assert_element(driver, xpath, clickable=False, return_many=False):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    if clickable:
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    if return_many:
        result = driver.find_elements(By.XPATH, xpath)
    else:
        result = driver.find_element(By.XPATH, xpath)

    return result


def click(driver, xpath):
    element = assert_element(driver, xpath, clickable=True)

    element.click()


def test_selenium_advanced(driver):
    driver.get('https://myfin.by/')
    find_card = assert_element(driver,
                               "//*[@href='/cards']")
    action = ActionChains(driver)
    action.move_to_element(find_card).perform()
    click(driver,
          "//div[div[contains(text(), 'Онлайн оформление карты')]]//*[contains(text(), 'Красная карта 2.0')]")

    driver.switch_to.window(driver.window_handles[-1])
    input_number = assert_element(driver,
                                  "//*[@type='tel']")
    # action.scroll_to_element(input_number).perform()
    input_number.send_keys("299402265")
    click(driver, "//*[@type='submit']")
    go_identification_string = assert_element(driver, "//*[contains(text(), 'Пройдите идентификацию')]")
    msi_button = assert_element(driver, "//button[contains(@class, 'button__accent_1xiwe')]")
    color_of_the_button = msi_button.value_of_css_property("background-color")
