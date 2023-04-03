from web_proships.modules.web_helpers.locators import PlayerMainPageLocators
from web_proships.modules.web_helpers.page_elements.hyperlink import HyperLink
from web_proships.modules.web_helpers.page_wrappers.player_intermediate_page import MonthlyStatisticPage
from web_proships.modules.web_helpers.page_wrappers.web_page import WebPage
from web_proships.modules.web_helpers.page_elements.element_searcher import ElementSearcher as Searcher


class GeneralStatisticPage(WebPage):
    @property
    def _all_date_links(self):
        return self.driver.find_elements(*PlayerMainPageLocators.LAST_DATE_LINKS)

    def last_days_links(self):
        return [HyperLink(Searcher.init_from_web_element(element), self.web_client, MonthlyStatisticPage)
                for element in self._all_date_links][0:5]

    def last_months_links(self):
        mark = 13 - len(self._all_date_links)
        return [HyperLink(Searcher.init_from_web_element(element), self.web_client, MonthlyStatisticPage)
                for element in self._all_date_links][5 - mark:10 - mark]

    def last_years_links(self):
        return [HyperLink(Searcher.init_from_web_element(element), self.web_client, MonthlyStatisticPage)
                for element in self._all_date_links][10:]
