from selenium import webdriver

from web_proships.modules.web_helpers.page_wrappers.clan_main_page import ClanMainPage

TIME_OUT = 10
ENABLE_CURSOR_POSITION_JS_SCRIPT = ""


class WebClient:
    def __init__(self, url):
        self._driver = None
        self.url = url

    @property
    def driver(self):
        if not self._driver:
            self._driver = webdriver.Chrome()
            return self._driver
        else:
            return self._driver

    def load_page(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(TIME_OUT)
        self.driver.maximize_window()
        return ClanMainPage(web_client=self)


# if __name__ == '__main__':
#     WebClient.load_page()
