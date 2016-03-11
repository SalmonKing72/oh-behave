import os, sys
from selenium import webdriver
from pyvirtualdisplay import Display

def before_all(context):
    browser = context.config.userdata.get('browser', 'phantomjs')

    if browser == 'chrome':
        if os.name != 'nt':
            display = Display(visible=0, size=(1280, 720))
            display.start()
        driver_arguments = {}
        driver_arguments['chrome_options'] = webdriver.ChromeOptions()
        driver_arguments['chrome_options'].add_argument('--no-sandbox')
        context.browser = webdriver.Chrome(**driver_arguments)
    else:
        context.browser = webdriver.PhantomJS()

    context.browser.implicitly_wait(3)


def after_all(context):  
    context.browser.quit()
