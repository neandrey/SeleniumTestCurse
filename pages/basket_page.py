from  .base_page import  BasePage
from .locators import BasketPageLocators



class BasketPage(BasePage):

    def should_be_empty_basket(self):
        """в корзине нет товаров"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY),\
        "Success basket is not empty, but should not be"

    def should_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE),\
        "Failed message, element should disappeared not be"