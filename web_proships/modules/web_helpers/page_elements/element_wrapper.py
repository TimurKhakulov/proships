class ElementWrapper:
    """
    Абстрактный класс инкапсулирующий любые элементы веб страницы
    """
    def __init__(self, elem_searcher, client, parent=None):
        self.searcher = elem_searcher
        self.client = client
        self.driver = client.driver
        self.parent = parent

    @property
    def web_searcher(self):
        return self.searcher.search()

    def get_attribute(self, value):
        return self.web_searcher.get_attribute(value)

    def click(self):
        self.web_searcher.click()

    def is_enabled(self):
        return self.web_searcher.is_enabled()

    def is_selected(self):
        return self.web_searcher.is_selected()

    def is_displayed(self):
        return self.web_searcher.is_displayed()
