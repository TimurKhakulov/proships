from web_proships.modules.web_helpers.page_elements.element_wrapper import ElementWrapper as Wrapper

VIEW_TEXT_TIMEOUT = 3


class Label(Wrapper):
    """
    Обертка для надписей
    """
    @property
    def value(self):
        return self.web_searcher.text
