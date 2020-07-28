from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CHECK_CART = (By.CSS_SELECTOR, 'span.btn-group a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_ADDRESS = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REPEAT_THE_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_PRODUCT_TO_CART = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE_ABOUT_SUCCESS_ADDING = (By.CSS_SELECTOR, '#messages div:first-child div.alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    CART_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')


class BasketPageLocators():
    EMPTY_CART = (By.CSS_SELECTOR, '#content_inner p')
    PRODUCTS_IN_THE_CART = (By.CSS_SELECTOR, 'h2.col-sm-6')
