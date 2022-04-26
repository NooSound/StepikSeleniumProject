from selenium.webdriver.common.by import By


#class MainPageLocators():


class LoginPageLocators():
    LOGIN_URL = "login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME = (By.XPATH , "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    ADDED_NAME_TO_BASKET = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    ADDED_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR , "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR , "#login_link_inc")
    BASKET_BTN = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    EMPTY_BASKET = (By.XPATH, "//p[contains(text(), 'empty')]")
    USER_ICON = (By.CSS_SELECTOR , ".icon-user")





