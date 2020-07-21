from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    BUTTON_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_OF_THE_PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, '#messages div:first-child div.alertinner strong')

