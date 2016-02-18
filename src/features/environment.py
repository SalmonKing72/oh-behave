import os, sys
from selenium import webdriver


def before_all(context):
    browser = context.config.userdata.get('browser', 'phantomjs')

    if browser == 'chrome':
        context.browser = webdriver.Chrome()
    else:
        context.browser = webdriver.PhantomJS()

    context.browser.implicitly_wait(3)


def after_all(context):  
    context.browser.quit()
