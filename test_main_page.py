from .pages.main_page import MainPage
from .pages.login_page import LoginPage




def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,
                    link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()

    page_login = LoginPage(browser, browser.current_url)
    page_login.should_be_login_url()
    page_login.should_be_login_form()
    page_login.should_be_register_form()
