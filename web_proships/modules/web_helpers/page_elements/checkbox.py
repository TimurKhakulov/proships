from web_proships.modules.web_helpers.page_elements.element_wrapper import ElementWrapper

TIMEOUT = 3


class CheckBox(ElementWrapper):

    def is_checked(self):
        return self.web_searcher.get_attribute("checked") not in (None, False)

    def is_unchecked(self):
        return not self.is_checked()

    def check(self):
        if self.is_unchecked():
            self.click()

    def uncheck(self):
        if self.is_checked():
            self.click()
