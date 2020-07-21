from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_PRODUCT_TO_BASKET), 'Кнопка добавления товара в корзину отсутствует'
        basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT_TO_BASKET)
        basket_button.click()

    def should_be_correct_name_of_product(self):
        assert self.is_element_present(
            *ProductPageLocators.NAME_OF_THE_PRODUCT_ADDED_TO_BASKET).text == , "Надпись об успешном добавлении товара в корзину отсутствует"

