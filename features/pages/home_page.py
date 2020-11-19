from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class HomePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='https://elmenus.com/')

    locators = {
            "sign_up_button" : (By.XPATH, '//*[@id="header"]/div/div[2]/div/div/button[2]'),
            "create_account_tab" : (By.XPATH, '//*[@id="signup-btn"]/a'),
            "login_link" : (By.XPATH, '//*[@id="header"]/div/div[2]/div/div/button[1]'),
            "profile_icon" : (By.XPATH, '//*[@id="header"]/div/div[2]/div/div/div/button'),
            "logout_button" : (By.XPATH, '//*[@id="header"]/div/div[2]/div/div/div/ul/li[3]/button'),

            # Login form
            "login_email" : (By.XPATH, '//*[@id="login-tab"]/form/div/div[1]/label/input'),
            "login_password" : (By.XPATH, '//*[@id="login-tab"]/form/div/div[2]/label/input'),
            "login_button" : (By.XPATH, '//*[@id="login-tab"]/form/div/button[1]'),

            # Sign up form
            "name" : (By.XPATH, '//*[@id="signup-tab"]/form/div/div[1]/label/input'),
            "email" : (By.XPATH, '//*[@id="signup-tab"]/form/div/div[2]/label/input'),
            "password" : (By.XPATH, '//*[@id="signup-tab"]/form/div/div[3]/label/input'),
            "create_account_button" : (By.XPATH, '//*[@id="signup-tab"]/form/div/button'),
            "after_sign_up" : (By.XPATH, '//*[@id="header"]/div/div[2]/div/div/div/button/span[2]'),

            # Search resturant form
            "find_resturant" : (By.XPATH, '//*[@id="app"]/section[1]/div[1]/div/div/form/div/div[1]/div/input'),
            "go_button" : (By.XPATH, '//*[@id="app"]/section[1]/div[1]/div/div/form/div/div[3]/button')
        }