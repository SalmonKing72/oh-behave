from page_objects import PageObject, PageElement


class DevcorrPage(PageObject):
    contact_button = PageElement(id_='contactButton')

    def contact_button_exists(self):
        return self.contact_button != None
