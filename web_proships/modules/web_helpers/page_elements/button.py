from web_proships.modules.web_helpers.page_elements.element_wrapper import ElementWrapper


class Button(ElementWrapper):

    def click(self):
        self.click()

    @property
    def is_present(self):
        return self.web_searcher.is_displayed()
