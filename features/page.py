class BasePage(object):
    url = None
    
    def __init__(self, context):
        self.context = context
        
    def navigate(self):
        self.context.browser.get(self.url)