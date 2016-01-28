from behave import *
from selenium import webdriver


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
    

@when('I visit google')
def step_impl(context):
    context.browser.get('http://www.google.com')  
 

@then('it should have a title "Google"')
def step(context):
    assert context.browser.title == "Google"
