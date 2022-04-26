from .Pages.product_page import ProductPage
from .Pages.basket_page import BasketPage
from .Pages.login_page import LoginPage
import pytest

# для одной ссылки:
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    """ открываем ссылку
        ищем кнопку добавить в корзину
        добавляем в корзину
        проверяем успешность
    """

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_to_basket()
    page.should_be_successfylly_added()



# для списка ссылок:
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_to_basket_btn()
#     page.add_to_basket()
#     page.should_be_successfylly_added()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """ открываем ссылку

        добавляем в корзину
        проверяем успешность
    """
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    """ открываем ссылку
        проверяем что нет сообщения об успешном добавлении товара в корзину
    """


    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """ открываем ссылку
        ищем кнопку добавить в корзину
        добавляем в корзину
        проверяем успешность
    """

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser , link)
    page.open()
    page.add_to_basket()
    page.should_be_dissapeared()


def test_guest_should_see_login_link_on_product_page(browser):
    """ открываем ссылку
        проверям наличие ссылки на логин страницу со страницы с товаром
    """

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """ открываем ссылку
        переходим на страницу логина
    """

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser , link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """ открываем ссылку
        переходим на страницу корзины
        ожидаем, что корзина пуста
    """

    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_cant_see_product_in_basket_opened_from_product_page()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """ параметры брауреза перед каждым тестом. идет регистрация и авторизация пользователя"""

        link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user()
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        """ открываем ссылку
            проверяем что нет сообщения об успешном добавлении товара в корзину
        """

        link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """ открываем ссылку
            ожидаем, что есть кнопка добавить в корзину
            добавляем товар в корзину
            ожидаем, что успешно добавлен товар в корзину
        """

        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_btn()
        page.add_to_basket()
        page.should_be_successfylly_added()



