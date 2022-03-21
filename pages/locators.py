from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM= (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM =(By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, "#add_to_basket_form")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    NAME_BOOK_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_BOOK = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BOOK_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(3) >.alertinner>p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "div.col-sm-2")
    BASKET_EMPTY_MESSAGE =(By.CSS_SELECTOR, "div#content_inner p")


