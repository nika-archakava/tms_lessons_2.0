from page_object.source_code.pages.base_element import BaseElement
from page_object.source_code.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.news_button = BaseElement(driver,
                                       "//*[@class='main-nav_link main-nav_link--straight'][contains(@href, 'stati')]/parent::*")
        self.find_cards = BaseElement(driver, "//*[@href='/cards']")
        self.red_card = BaseElement(driver,
                                    "//div[div[contains(text(), 'Онлайн оформление карты')]]//*[contains(text(), 'Красная карта 2.0')]")
