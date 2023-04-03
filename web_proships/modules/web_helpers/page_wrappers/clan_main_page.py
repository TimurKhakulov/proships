from web_proships.modules.web_helpers.locators import MainPageLocators
from web_proships.modules.web_helpers.page_elements.element_searcher import ElementSearcher as Searcher
from web_proships.modules.web_helpers.page_elements.hyperlink import HyperLink
from web_proships.modules.web_helpers.page_wrappers.player_main_page import GeneralStatisticPage
from web_proships.modules.web_helpers.page_wrappers.web_page import WebPage


class ClanMainPage(WebPage):
    @property
    def _players_links(self):
        return self.driver.find_elements(*MainPageLocators.PLAYERS_LINKS)

    def players_links(self):
        return [HyperLink(Searcher.init_from_web_element(element),
                          self.web_client, GeneralStatisticPage) for element in self._players_links]
