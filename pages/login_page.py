from .base_page import BasePage
from .locators import  LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #print(self.url)
        #print(self.browser.current_url.find( "login"))
        assert self.url.find("login") != -1, "URL not 'login' in string"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_address = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        email_address.send_keys(email)
        print(email)
        password_first = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_first.send_keys(password)
        print(password_first)
        password_second = self.browser.find_element(*LoginPageLocators.PASSWORD_DUPLICAT)
        password_second.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        print(password_second)
        button_register.click()







