from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):
    def cart_should_be_empty_of_items(self):
        """Негативная проверка. Чекает, что селектор, который появляется при добавлении
        товара в корзину отсутствует на странице (т.к. товаров в корзине нет)"""
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_THE_CART), 'Корзина должна быть пустая,' \
                                                                                      'т.к. в неё не добавляли товаров'

    def message_about_cart_is_empty(self):
        """Позитивная проверка. Чекает, что сообщение 'Ваша корзина пустая' отображается на странице"""
        assert "Your basket is empty." in self.browser.find_element(
            *BasketPageLocators.EMPTY_CART).text, 'Корзина не пуста'
