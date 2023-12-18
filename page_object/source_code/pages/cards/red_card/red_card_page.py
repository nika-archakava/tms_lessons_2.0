from page_object.source_code.pages.base_element import BaseElement
from page_object.source_code.pages.base_page import BasePage


class RedCardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.input_number = BaseElement(driver, "//*[@type='tel']")
        self.submit_button = BaseElement(driver, "//*[@type='submit']")
        self.identification_string = BaseElement(driver, "//*[@class='title']")
        self.msi_button = BaseElement(driver, "//button[@type='button']")
