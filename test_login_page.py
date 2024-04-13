from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_login_register_page(browser):
    authorization = LoginPage(browser, link)
    authorization.open()
    authorization.should_be_login_page()

