from selenium import webdriver
  
def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(3)
  
def after_all(context):  
    context.browser.quit() 