from behave import *
import logging
from nose.tools import assert_equals, assert_true
from features.pages.home_page import *
from features.pages.base_page import *
from features.pages.e2e_objects import *
from faker import Faker

fake = Faker()

@given(u'i click on sign up button')
def step_impl(context):
    context.execute_steps(u"""given i visit elmenus.com as a guest user """)
    page = HomePage(context)
    page.sign_up_button.click()

@when(u'i fill in the form')
def step_impl(context):
    page = HomePage(context)
    page.create_account_tab.click()
    page.name.send_keys(fake.name())
    page.email.send_keys(fake.email())
    page.password.send_keys(fake.password())
    
@when(u'press create account')
def step_impl(context):
    page = HomePage(context)
    page.create_account_button.click()
    
@then(u'i signed up successfully')
def step_impl(context):
    page = HomePage(context)
    assert "Hello" in page.after_sign_up.text