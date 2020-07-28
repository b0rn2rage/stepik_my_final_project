import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        """Переход на страницу логина"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Ссылка на логин не отображается на странице"
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_cart(self):
        """Переход в корзину по кнопке "Посмотреть корзину" """
        assert self.is_element_present(*BasePageLocators.CHECK_CART), "Кнопка 'Посмотреть корзину' " \
                                                                      "отсутствует на странице"
        check_cart_button = self.browser.find_element(*BasePageLocators.CHECK_CART)
        check_cart_button.click()

    def is_element_present(self, how, what):
        """Проверка наличия элемента на странице"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Проверка того, что элемент отсутствует на странице"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            """Если случается TimeoutException (элемента нет на странице), то тест успешно пройдет - вернется True"""
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """Проверка, что элемент исчезает со страницы"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            """В течение 4 секунд проверяет наличие элемента на странице.
                Если элемент не исчез, то False и тест провален"""
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        """Прохождение капчи"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_login_link(self):
        """Проверка наличия на странице ссылки, которая ведет на страницу логина"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Ссылка на логин не отображается на странице"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), 'Иконка юзера не отображается, возможно ' \
                                                                     'пользователь не авторизован'
