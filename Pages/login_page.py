from .base_page import BasePage
from .locators import LoginPageLocators
import random
from string import ascii_letters, digits
import time


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL in self.browser.current_url, "wrong url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def generate_password(self):                                                          # генератор паролей: буквы-цифры, строчные-заглавные, длина 10.
        LETTER = ''.join((set(ascii_letters) | set(digits)))
        pwd = ''
        while len(pwd) != 10:
            pwd += random.choice(LETTER)
        return pwd

    def register_new_user(self):                                                          # регистрация нового пользователя.
        password = self.generate_password()
        email = str(time.time()) + "@fakemail.org"

        self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()




