from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage
from .Pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    """Гость открывает главную страницу
       Переходит на страницу логина ссылке в шапке сайта
       Ожидаем, что страница логина корректна"""


    link = "http://selenium1py.pythonanywhere.com"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):

    '''Гость открывает главную страницу
    Переходит в корзину по кнопке в шапке сайта
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста '''

    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_cant_see_product_in_basket_opened_from_main_page()





