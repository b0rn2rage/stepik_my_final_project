from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE_ABOUT_SUCCESS_ADDING = (By.CSS_SELECTOR, '#messages div:first-child div.alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
