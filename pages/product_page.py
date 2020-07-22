from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # Проверям, что кнопка добавления товара в корзину есть на странице, нажатие на кнопку (добавляем товар в корзину)
    def add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_PRODUCT_TO_BASKET), 'Кнопка добавления товара в корзину отсутствует'
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_BASKET)
        basket_button.click()

    def should_be_message_about_adding(self):
        # Сообщение об успешном добавлении товара в корзину
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ABOUT_SUCCESS_ADDING), 'Сообщение о добавлении товара в корзину отсутствует'
        alert_message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_SUCCESS_ADDING).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # Сообщение о добавлении товара соответствует именно тому товару, который был добавлен в корзину
        current_url = self.browser.current_url
        assert alert_message == product_name, f'Сообщение о добавлении товара не совпадает с именем товара, который был добавлен в корзину. Cсылка на товар – {current_url}'

    def total_cost_of_the_basket(self):
        # Сообщение о стоимости корзины отображается
        assert self.is_element_present(
            *ProductPageLocators.BASKET_PRICE), 'Сообщение со стоимостью товаров в корзине отсутствует'
        basket_price_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_price_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Стоимость товаров в корзине равна стоимости товара, добавленного в корзину
        assert basket_price_message == product_price_message, 'Стоимость товаров в корзине равна стоимости добавленного товара'

    def should_not_be_success_message(self):
        # Проверка, что сообщение об успешном добавлении товара в корзину не должно появиться в течение определенного времени
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_SUCCESS_ADDING), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        # Проверка, что элемент исчезает с страницы
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_SUCCESS_ADDING), \
            "Message is displayed on the page, but should not be"
