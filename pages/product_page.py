from  .base_page import  BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math



class ProductPage(BasePage):
    def add_to_basket_button(self):
        basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        basket.click()

    def should_be_add_button_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD), "Basket button is not present on page."

    def price_items_is_basket_conside(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        basket_price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_BASKET).text
        assert  price_book == basket_price_book, f"Price of book {price_book} and Price of book_basket " \
                                                 f"{basket_price_book} not equal"

    def name_items_is_basket_conside(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        basket_name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK_BASKET).text
        assert  name_book == basket_name_book, f"Name of book {name_book} and " \
                                               f"name of book_basket {basket_name_book} not equal"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        """нет элемента подтверждающего сообщения"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Failed message, element should disappeared not be"
