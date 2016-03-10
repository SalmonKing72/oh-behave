from behave import *
from pages import DevcorrPage


def setPage(context):
    context.page = DevcorrPage(context.browser, root_uri="http://devcorr.com")


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
    

@when('I visit devcorr')
def step_impl(context):
    setPage(context)
    context.page.get('/')
 

@then('it should have a title "{title}"')  
def step(context, title):  
    assert context.browser.title == title

@then('I should see the contact button')
def step(context):
    assert context.page.contact_button_exists