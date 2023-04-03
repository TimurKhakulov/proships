from web_proships.modules.web_helpers.page_elements.label import Label
from web_proships.modules.web_helpers.page_elements.table import Table, TableFilter
from web_proships.modules.web_helpers.page_elements.element_searcher import ElementSearcher as Searcher


class ShipsTable(Table):
    def __init__(self, table, web_client):
        super().__init__(table, web_client)
        self.web_client = web_client
        self.table = table
        self.rows = None

    def is_int(self, str_element):
        try:
            int(str_element)
            return True
        except ValueError:
            return False

    def is_float(self, str_element):
        try:
            float(str_element)
            return True
        except ValueError:
            return False

    def column_names(self, last_battle=False):
        table_header = [Label(Searcher.init_from_web_element(element), self.web_client)
                        for element in self.table_header]

        names = []
        for title in table_header:
            if title.value is not None:
                if title.is_displayed():
                    names.append(title.value)
        if last_battle:
            names.append('время')
        return names

    def edit_row_elements(self, row_edit):
        for position in range(len(row_edit)):
            if row_edit[position].isnumeric():
                row_edit[position] = int(row_edit[position])
            else:
                if self.is_float(row_edit[position]):
                    row_edit[position] = float(row_edit[position])

    @property
    def table_filters(self):
        return [TableFilter(Searcher.init_from_web_element(_filter), self.web_client)
                for _filter in self.table_filter]

    def sort_filters(self, user_filters):
        for f in self.table_filters:
            if f.checkbox.get_attribute('data-column') in user_filters:
                if not f.checkbox.is_checked():
                    f.click()
            else:
                if f.checkbox.is_checked():
                    f.click()

    def table_rows(self, len_row, ship_name_position):
        self.rows = []
        for row in self.str_rows:
            row_edit = row.text.split()
            if len(row_edit) != len_row:
                words_in_name = len(row_edit) - len_row + 1

                union_name = []
                for i in range(words_in_name):
                    union_name.append(row_edit[ship_name_position + i])
                union_name = ' '.join(union_name)

                del row_edit[ship_name_position:ship_name_position + words_in_name]

                row_edit.insert(ship_name_position, union_name)

                self.edit_row_elements(row_edit)

                self.rows.append(row_edit)
            else:
                self.edit_row_elements(row_edit)

        return self.rows

