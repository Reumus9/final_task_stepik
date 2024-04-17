import pytest 
from pages.product_page import ProductPage
from pages.product_locators import ProductLocators

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product = ProductPage(browser, link)
    product.open()
    product.add_to_basket()
    assert product.is_not_element_present(*ProductLocators.BASKET_NAME_BOOK), "упал первый тест"

def test_guest_cant_see_success_message(browser):
    product = ProductPage(browser, link)
    product.open()
    assert product.is_not_element_present(*ProductLocators.BASKET_NAME_BOOK), "упал второй тест"

@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser):
    product = ProductPage(browser, link)
    product.open()
    product.add_to_basket()
    assert product.is_disappeared(*ProductLocators.BASKET_NAME_BOOK), "упал третий тест"