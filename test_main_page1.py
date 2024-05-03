from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

def test_guest_can_go_to_login_page(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.view_basket()
    page.check_message_empty_basket()
    page.negative_check_message_empty_basket()

#Гость открывает главную страницу 
#Переходит в корзину по кнопке в шапке сайта
#Ожидаем, что в корзине нет товаров
#Ожидаем, что есть текст о том что корзина пуста 