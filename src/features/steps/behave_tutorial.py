from behave import *
from pages import GooglePage

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
    page = GooglePage(context)
    page.navigate()
 

@then('it should have a title "{title}"')  
def step(context, title):  
   assert context.browser.title == title