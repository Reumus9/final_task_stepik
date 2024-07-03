import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.product_locators import ProductLocators
import faker 
from pages.login_page import LoginPage

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
    product = ProductPage(browser, link, 3)
    product.open()
    title = product.get_title_book()
    price = product.get_price_book()
    product.add_to_basket()
    product.solve_quiz_and_get_code()
    product.product_check(title, price)
    

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()



def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.view_basket()
    page.check_message_empty_basket()
    page.negative_check_message_empty_basket()

@pytest.mark.new
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        f = faker.Faker()
        email = f.email()
        password = f.password(length = 12)
        user = LoginPage(browser, "http://selenium1py.pythonanywhere.com/")
        user.open()
        user.go_to_login_page()
        user.register_new_user(email, password)
        user.should_be_authorized_user()
        
        
    
    def test_user_can_add_product_to_basket(self, browser):
        product = ProductPage(browser, "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/", 3)
        product.open()
        title = product.get_title_book()
        price = product.get_price_book()
        product.add_to_basket()
        product.product_check(title, price)
        
    def test_user_cant_see_success_message(self, browser):
        product = ProductPage(browser, "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
        product.open()
        assert product.is_not_element_present(*ProductLocators.BASKET_NAME_BOOK), "упал второй тест"