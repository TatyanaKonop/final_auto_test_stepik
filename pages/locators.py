from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "url login page не совпадает"
    