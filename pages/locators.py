from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE_ABOUT_SUCCESS_ADDING = (By.CSS_SELECTOR, '#messages div:first-child div.alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')

