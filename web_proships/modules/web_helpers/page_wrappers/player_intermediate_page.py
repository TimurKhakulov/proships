from web_proships.modules.web_helpers.locators import PlayerIntermediatePageLocators
from web_proships.modules.web_helpers.page_elements.label import Label
from web_proships.modules.web_helpers.page_wrappers.ships_table import ShipsTable
from web_proships.modules.web_helpers.page_wrappers.web_page import WebPage
from web_proships.modules.web_helpers.page_elements.element_searcher import ElementSearcher as Searcher


class MonthlyStatisticPage(WebPage):
    @property
    def player_name(self):
        def find():
            return self.web_client.driver.find_element(*PlayerIntermediatePageLocators.PLAYER_NAME)
        return Label(Searcher(find), self.web_client)

    def general_statistic_table(self):
        pass

    def class_statistic_table(self):
        pass

    @property
    def ship_statistic_table(self):
        def find():
            return self.web_client.driver.find_element(*PlayerIntermediatePageLocators.SHIP_STATISTIC_TABLE)
        return ShipsTable(Searcher(find()), self.web_client)
