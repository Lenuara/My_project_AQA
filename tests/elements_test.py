# первичная проверка работоспособности - сайт открывается и закрывается через 3 сек
# import time
# from pages.base_page import BasePage
#
# def test(driver):
#     page = BasePage(driver, 'https://www.google.com')
#     page.open()
#     time.sleep(3)
import time

from pages.elements_page import TextBoxPage, CheckBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            # print(output_name)
            # print(output_email)
            # print(output_cur_addr)
            # print(output_per_addr)
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the current address does not match"
            assert permanent_address == output_per_addr, "the permanent address does not match"

        # def test_text_box(self, driver):
        #     text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        #     text_box_page.open()
        #     input_data = text_box_page.fill_all_fields()
        #     output_data = text_box_page.check_filled_form()
        #
        #     assert input_data == output_data

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()













