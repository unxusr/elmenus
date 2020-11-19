from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class e2e_objects(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='https://elmenus.com/')

    locators = {
            "sign_up_button" : (By.XPATH, '//*[@id="header"]/div/div[2]/div/div/button[2]'),
            "find_resturant" : (By.XPATH, '//*[@id="app"]/section[1]/div[1]/div/div/form/div/div[1]/div/input'),
            "go_button" : (By.XPATH, '//*[@id="app"]/section[1]/div[1]/div/div/form/div/div[3]/button'),
            "page_header" : (By.CLASS_NAME, 'col-title'),
            "restaurants_name" : (By.XPATH, '//*[@id="rest-list-col"]/div[2]/div/div/div/div[2]/div[2]/h3/a'),
            "menu_item" : (By.XPATH, '//*[@id="topDishes-0"]/div/div[5]/div[1]/div[1]/h5'),
            "mac" : (By.XPATH, '//*[@id="rest-list-col"]/div[2]/div/div/div/div[2]/a'),
            "menu_page" : (By.XPATH, '//*[@id="menu-tab"]/h4/span'),
            "big_mac" : (By.XPATH, '//*[@id="topDishes-0"]/div/div[5]/div[1]/div[1]/a'),
            "special_instructions" : (By.XPATH, '/html/body/div[3]/div[2]/div[3]/div[4]/div[1]/div[3]/div/div/div/div[2]/div/div/div[2]/div[2]/div[7]/input'),
            "add_to_basket" : (By.XPATH, '//*[@id="item-view-modal"]/div/div/div[2]/div[2]/button'),
            "login_modal" : (By.XPATH, '//*[@id="create-basket"]/div/div[1]/h2' ),
            "create_account" : (By.XPATH, '//*[@id="basket-signup-tab-btn"]/a'),
            "create_account_home_page" : (By.XPATH, '//*[@id="signup-btn"]/a'),
            "name" : (By.XPATH, '//*[@id="basket-signup-tab"]/form/div/div[1]/label/input'),
            "email" : (By.XPATH, '//*[@id="basket-signup-tab"]/form/div/div[2]/label/input'),
            "password" : (By.XPATH, '//*[@id="basket-signup-tab"]/form/div/div[3]/label/input'),
            "account_creation_button" : (By.XPATH, '//*[@id="basket-signup-tab"]/form/div/button'),
            "search_for_location" : (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/div[1]/div[2]/label/input'),
            "suggested_location" : (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/div[1]/ul/li[6]/button/span[2]'),
            "choose_selected_location" : (By.XPATH, '//*[@id="zones-list"]/ul/li/button'),
            "order_details" : (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[1]/div/h2'),
            "go_to_checkout_button" : (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[1]/div/div[5]/button[1]'),
            "address_info" : (By.XPATH, '//*[@id="addressForm"]/div/div[2]/div[2]/label/input'),
            "building_no" : (By.XPATH , '//*[@id="addressForm"]/div/div[2]/div[3]/div[1]/label/input'),
            "floor_no" : (By.XPATH, '//*[@id="addressForm"]/div/div[2]/div[3]/div[2]/label/input'),
            "apartment_no" : (By.XPATH, '//*[@id="addressForm"]/div/div[2]/div[3]/div[3]/label/input'),
            "mobile_no" : (By.XPATH, '//*[@id="addressForm"]/div/div[2]/div[4]/label/input'), 
            "map" : (By.XPATH, '//*[@id="addressForm"]/div/div[2]/div[1]'),
            "save_address" : (By.XPATH, '//*[@id="addressForm"]/button[1]'),
            "deliver_to_this_address_button" : (By.XPATH, '//*[@id="step-1"]/div/ul/li/div/button'),
            "place_order" : (By.XPATH, '//*[@id="checkout-modal"]/div/div/div/div[2]/div/div/div[1]/button')
        }