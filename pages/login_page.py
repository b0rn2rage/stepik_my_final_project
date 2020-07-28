import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        assert self.is_element_present(*LoginPageLocators.EMAIL_ADDRESS), "Поле 'Адрес электронной почты' \
                                                                          'отсутствует на странице"
        textbox_for_email_address = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        textbox_for_email_address.send_keys(self.email)
        assert self.is_element_present(*LoginPageLocators.PASSWORD), "Поле 'Пароль' отсутствует на странице"
        textbox_for_first_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        textbox_for_first_password.send_keys(self.password)
        assert self.is_element_present(*LoginPageLocators.REPEAT_THE_PASSWORD), "Поле 'Повторите пароль отсутствует' \
                                                                                'на странице"
        textbox_for_second_password = self.browser.find_element(*LoginPageLocators.REPEAT_THE_PASSWORD)
        textbox_for_second_password.send_keys(self.password)
        assert self.is_element_present(*LoginPageLocators.SUBMIT_BUTTON), "Кнопка 'Зарегистрироваться' отсутствует" \
                                                                          "на странице"
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()
        time.sleep(5)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'Надпись login отсутствует в url страницы'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина отсутствует на странице"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации отсутствует на странице"
