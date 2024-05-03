from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators ():
    UNDER_URL = "login"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#register_form")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LOC = (By.CSS_SELECTOR, ".btn-group a")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")