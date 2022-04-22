from .base_page import BasePage
from .locators import ProductPageLocators




class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        button.click()
        self.solve_quiz_and_get_code()



    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "No button"


    def should_be_successfylly_added(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_NAME_TO_BASKET).text
        assert added_product_name == product_name, "No success added product"

    def should_be_correct_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE)
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRICE)
        assert product_price == added_product_price, 'incorrect price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE) , \
            "Success message is presented, but should not be"

    def should_be_dissapeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE) , \
            "Success message is not disappeared"

