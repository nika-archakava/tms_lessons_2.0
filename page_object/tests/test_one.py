from time import sleep

from page_object.source_code.pages.cards.red_card.red_card_page import RedCardPage
from page_object.source_code.pages.help_functions import from_rgba_to_hex
from page_object.source_code.pages.main.main_page import MainPage


class TestClass:
    def test_first_case(self, driver):
        main_page = MainPage(driver)
        red_card_page = RedCardPage(driver)
        main_page.find_cards.hover()
        main_page.red_card.custom_click()
        driver.switch_to.window(driver.window_handles[-1])
        red_card_page.input_number.assert_element().send_keys("299402265")
        red_card_page.submit_button.custom_click()
        for i in range(10):
            actual_ident_text = red_card_page.identification_string.assert_element().text
            if actual_ident_text == 'Пройдите идентификацию':
                break
            sleep(1)
        else:
            raise Exception("Надпись 'Пройдите идентификацию' не отображается на странице")
        assert red_card_page.msi_button.assert_element().is_displayed(), \
            "Кнопка 'Перейти в МСИ' не отображается на странице!"

        current_color = red_card_page.msi_button.assert_element().value_of_css_property("background-color")

        current_color_hex = from_rgba_to_hex(current_color)
        assert current_color_hex == '#ef3124', \
            'Цвет кнопки "Перейти в МСИ" не соответсвует заявленному #ef3124'
