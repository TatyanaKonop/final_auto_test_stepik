from .base_page import BasePage
from .locators import LoginPageLocators
from .main_page import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        print(self.browser.current_url)
        assert self.browser.current_url in LoginPageLocators.LOGIN_URL, f"url login page is wrong {self.browser.current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "there isn't login form"
        print('there is a login form')
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "there isn't a register form"
        print('there is a register form')