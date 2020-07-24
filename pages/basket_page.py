from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):
    def cart_should_be_empty_of_items(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_THE_CART), 'Корзина должна пустая,' \
                                                                                      'т.к. в неё не добавляли товаров'

    def message_about_cart_is_empty(self):
        '''Допилить реализацию'''
        assert "Ваша корзина пуста" in self.is_element_present(*BasketPageLocators.EMPTY_CART), 'Корзина не пуста'
