from behave import *
import logging
from nose.tools import assert_equals, assert_true
from features.pages.home_page import *
from features.pages.base_page import *
from features.pages.e2e_objects import *
from faker import Faker

fake = Faker()

@given(u'i visit elmenus.com as a guest user')
def step_impl(context):
    page = e2e_objects(context)
    page.visit('https://elmenus.com')
    assert_equals(page.base_url, "https://elmenus.com/")

@when(u'i type a "McDonald\'s" in the search field')
def step_impl(context):
    page = e2e_objects(context)
    page.find_resturant.send_keys("McDonalds")

@when(u'i press "go" button')
def step_impl(context):
    page = e2e_objects(context)
    page.go_button.click()
    assert_equals(page.page_header.text, "1 Restaurants")
    assert_equals(page.restaurants_name.text, "McDonald's")

@when(u'i click on "McDonald\'s"')
def step_impl(context):
    page = e2e_objects(context)
    page.mac.click()

@then(u'i can see all "McDonald\'s" menu items')
def step_impl(context):
    page = e2e_objects(context)
    assert_equals(page.menu_page.text, "Menu")
    assert_equals(page.menu_item.text, "Big Mac")

@then(u'i can select item from McDonald\' menu')
def step_impl(context):
    page = e2e_objects(context)
    page.big_mac.click()
    page.special_instructions.send_keys("Catch you! This is a fake order by Moamen Hussein, Production test")
    page.add_to_basket.click()

@then(u'i stopped by the login modal')
def step_impl(context):
    page = e2e_objects(context)
    assert_equals(page.login_modal.text, "Please, Login first!")

@then(u'i create new account')
def step_impl(context):
    page = e2e_objects(context)
    page.create_account.click()
    page.name.send_keys(fake.name())
    page.email.send_keys(fake.email())
    page.password.send_keys(fake.password())
    page.account_creation_button.click()

@then(u'i select my location')
def step_impl(context):
    page = e2e_objects(context)
    page.suggested_location.click()
    page.choose_selected_location.click()
    # Some times the order summary and go to check out button dont appear
    # and i have to reload the page to continue the test
    # so this is a work around to reload the page only
    if not page.order_details:
        page.reload()
        logging.info("Force reload!")
    
    page.go_to_checkout_button.click()

@then(u'i fill in my address information')
def step_impl(context):
    page = e2e_objects(context)
    page.address_info.send_keys('Gezira club')
    page.double_click(page.map)
    page.building_no.send_keys('1')
    page.floor_no.send_keys('2')
    page.apartment_no.send_keys('3')
    page.mobile_no.send_keys('01141482840')
    # Change the number above  ^  so you
    # can receive the the verification code 
    # and uncommnet the below line 
    
    # page.save_address.click()

@then(u'i placed the order sucessfully')
def step_impl(context):
    page = e2e_objects(context)
    #page.deliver_to_this_address_button.click()
    # I could place the order but this will lead to fake an order to a fake place 
    #page.place_order.click()
    #time.sleep(10)  # Sometimes it delayes to send verification code

