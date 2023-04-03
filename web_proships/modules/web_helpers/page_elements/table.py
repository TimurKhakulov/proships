from web_proships.modules.web_helpers.locators import TableContent, PlayerIntermediatePageLocators, StatisticTableFilter
from web_proships.modules.web_helpers.page_elements.checkbox import CheckBox
from web_proships.modules.web_helpers.page_elements.element_wrapper import ElementWrapper
from web_proships.modules.web_helpers.page_elements.label import Label
from web_proships.modules.web_helpers.page_elements.element_searcher import ElementSearcher as Searcher


class Table(ElementWrapper):
    @property
    def table_header(self):
        return self.driver.find_elements(*TableContent.TABLE_HEADER)

    @property
    def table_filter(self):
        return self.driver.find_elements(*PlayerIntermediatePageLocators.TABLE_FILTERS)

    @property
    def str_rows(self):
        return self.driver.find_elements(*TableContent.TABLE_ROWS)


class TableFilter(ElementWrapper):
    @property
    def checkbox(self):
        def find():
            return self.web_searcher.find_element(*StatisticTableFilter.CHECKBOX)
        return CheckBox(Searcher(find), self.client)

    @property
    def label(self):
        def find():
            return self.web_searcher.find_element(*StatisticTableFilter.LABEL)
        return Label(Searcher(find), self.client)
