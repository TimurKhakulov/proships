from web_proships.modules.web_helpers.web_client import WebClient

URL = 'https://www.yandex.ru'


class TestMainPage:
    main_page = None

    @classmethod
    def setup_class(cls):
        TestMainPage.main_page = WebClient(URL).load_page()

    def test_find_button(self):
        assert TestMainPage.main_page.find_button.is_present(), "Button not found"
        assert TestMainPage.main_page.find_button.is_clicable(), "Button not found"
        assert TestMainPage.main_page.prognoz.get_attribute('href'), 'Link out'
        print(TestMainPage.main_page.prognoz.get_attribute('href'))


if __name__ == "__main__":
    a = TestMainPage()
    a.setup_class()
    a.test_find_button()
