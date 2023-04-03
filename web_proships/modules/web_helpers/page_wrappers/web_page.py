class WebPage:
    """
    Абстрактный класс инкапсулирующий веб страницу
    """
    def __init__(self, web_client):
        self.web_client = web_client
        self.driver = web_client.driver

    @property
    def current_url(self):
        return self.driver.current_url
