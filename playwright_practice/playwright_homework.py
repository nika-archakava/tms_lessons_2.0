from playwright.sync_api import expect


def validate_phone_number(phone_number):
    if (len(phone_number) == 17 and
            phone_number[0:8] in ['8 (017) ', '8 (025) ', '8 (029) ', '8 (033) ', '8 (044) '] and
            phone_number[11] == '-' and
            phone_number[14] == '-' and
            phone_number[8:11].isdigit() and
            phone_number[12:14].isdigit() and
            phone_number[15:17].isdigit()
    ):
        return True
    else:
        return False


class TestClassPlaywright:
    def test_homework_playwright(self, page):
        page.goto("https://blizko.by/")
        page.get_by_role("link", name="Каталог").click()
        page.get_by_text("Дом", exact=True).click()
        page.get_by_role("link", name="Товары для дома").click()
        phone_button = page.locator("xpath=(//a[text()='Телефоны'])").first
        phone_button.click()

        modal_title = page.locator("xpath=(//*[@id='modalSet']//div[@class='ttl'])")
        expect(modal_title).to_be_visible()
        title_font_weight_expected = '700'
        title_font_weight_actual = modal_title.evaluate(
            "(e) => {return"
            " window.getComputedStyle(e).getPropertyValue('font-weight');"
            "}"
        )
        assert title_font_weight_actual == title_font_weight_expected

        modal_address = page.locator("xpath=(//*[@id='modalSet']//div[@class='descr'])")
        expect(modal_address).to_be_visible()

        modal_close_button = page.locator("xpath=(//a[@class='modal__close'])")
        expect(modal_close_button).to_be_visible()
        expect(modal_close_button).to_be_enabled()

        modal_footer = page.locator("xpath=(//*[@id='modalSet']//div[@class='pmi__footer'])")
        expect(modal_footer).to_have_text('Пожалуйста, сообщите администратору, что нашли этот телефон на Blizko.by')

        modal_numbers_list = page.locator("xpath=(//*[@id='modalSet']//div[@class='pmi__list']/a)").all()
        for number in modal_numbers_list:
            expect(number).to_be_visible()
            expect(number).to_be_enabled()
            number_text = number.inner_text()
            assert validate_phone_number(number_text)
