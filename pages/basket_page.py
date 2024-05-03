from .base_page import BasePage
from .locators import BasePageLocators
import pytest

class BasketPage(BasePage):
    def check_message_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY_MESSAGE), "сообщение о пустой корзины отсувствует"
    
    @pytest.mark.xfail
    def negative_check_message_empty_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_EMPTY_MESSAGE) == False, "сообщение о пустой коризине присувствует"
