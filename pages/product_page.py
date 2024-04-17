from .base_page import BasePage
from .product_locators import ProductLocators
class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductLocators.BASKET_LOC).click()

    def get_title_book(self):
        return self.browser.find_element(*ProductLocators.NAME_BOOK_LOC).text
    
    def get_price_book(self):
        return self.browser.find_element(*ProductLocators.PRICE_LOC).text
    
    def get_title_book_in_basket(self):
        return self.browser.find_element(*ProductLocators.BASKET_NAME_BOOK).text
    
    def get_price_basket(self):
        return self.browser.find_element(*ProductLocators.BASKET_PRICE).text
    
    def product_check(self,title, price):
        price_basket = self.get_price_basket()
        title_book = self.get_title_book_in_basket()
        assert title == title_book, "название книги не совпадает в корзине"
        assert price_basket == price, "цена книги не совпадает со стоимостью корзины" 