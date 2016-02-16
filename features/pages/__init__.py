class BasePage(object):
    url = None
    
    def __init__(self, context):
        self.context = context
        
    def navigate(self):
        self.context.browser.get(self.url)

class GooglePage(BasePage):
    url = 'http://www.google.com'