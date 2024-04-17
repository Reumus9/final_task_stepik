from selenium.webdriver.common.by import By

class ProductLocators():
    BASKET_LOC = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_BOOK_LOC = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_LOC = (By.CSS_SELECTOR, ".price_color")
    BASKET_NAME_BOOK = (By.CSS_SELECTOR, "#messages :nth-child(2) strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages :nth-child(3) strong")