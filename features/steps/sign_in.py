from behave import *
import logging
from nose.tools import assert_equals, assert_true
from features.pages.home_page import *
from features.pages.base_page import *
from features.pages.e2e_objects import *
from faker import Faker

fake = Faker()
email = fake.email()
password = fake.password()
name = fake.name()

@given(u'i created account successfully')
def step_impl(context):
    context.execute_steps(u"""given i visit elmenus.com as a guest user """)
    page = HomePage(context)
    page.sign_up_button.click()
    page.create_account_tab.click()
    page.name.send_keys(name)
    page.email.send_keys(email)
    page.password.send_keys(password)
    page.create_account_button.click()
    assert "Hello" in page.after_sign_up.text
    page.profile_icon.click()
    page.logout_button.click()

@when(u'i press login button')
def step_impl(context):
    page = HomePage(context)
    page.login_link.click()
    page.login_email.send_keys(email)
    page.login_password.send_keys(password)
    page.login_button.click()
    time.sleep(1)


@then(u'i logged in successfully')
def step_impl(context):
    page = HomePage(context)
    assert name in page.after_sign_up.text