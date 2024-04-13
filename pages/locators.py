from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators ():
    UNDER_URL = "login"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#register_form")
