from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):

    def should_cant_see_product_in_basket_opened_from_main_page(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET), "Basket is not empty"



    def should_cant_see_product_in_basket_opened_from_product_page(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET), "Basket is not empty"


    def go_to_basket_page(self):
        button = self.browser.find_element(*BasePageLocators.BASKET_BTN)
        button.click()


# default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a