from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import traceback
import time

class BasePage(object):

    def __init__(self, browser, base_url='https://elmenus.com/'):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 30

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def current_url(self):
        return self.browser.current_url()

    def visit(self,url):
        self.browser.get(url)

    def hover(self,element):
            ActionChains(self.browser).move_to_element(element).perform()
            # I don't like this but hover is sensitive and needs some sleep time
            time.sleep(5)

    def double_click(self, element):
        ActionChains(self.browser).double_click(element).perform()

    def reload(self):
        self.browser.refresh()
        
    #def wait_for_xpath(self, element):
    #    element = WebDriverWait(self.browser, 10).until(
    #            EC.presence_of_element_located((By.XPATH, element)))
    #    return element


    def __getattr__(self, what):
        try:
            if what in self.locators.keys():
                try:
                    element = WebDriverWait(self.browser,self.timeout).until(
                        EC.presence_of_element_located(self.locators[what])
                    )
                except(TimeoutException,StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    element = WebDriverWait(self.browser,self.timeout).until(
                        EC.visibility_of_element_located(self.locators[what])
                    )
                except(TimeoutException,StaleElementReferenceException):
                    traceback.print_exc()
                # I could have returned element, however because of lazy loading, I am seeking the element before return
                return self.find_element(*self.locators[what])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)

    def method_missing(self, what):
        print(f"No {what} here!")

    