from web_proships.modules.web_helpers.page_elements.element_wrapper import ElementWrapper


class HyperLink(ElementWrapper):
    def __init__(self, element, client, page_wrapper=None):
        super().__init__(element, client)
        self.page_wrapper = page_wrapper

    @property
    def url(self):
        return self.get_attribute('href')

    def open(self):
        self.click()
        if self.page_wrapper:
            return self.page_wrapper(self.client)
