# -*- coding: utf-8 -*-

import pandas as pd
from web_proships.modules.web_helpers.web_client import WebClient


URL = 'https://proships.ru/stat/ru/c/434567-RUSHB'
ALL_FILTER_NAMES = {'0': 'Класс',
                    '1': 'Нация',
                    '2': 'Уровень',
                    '3': 'Корабль',
                    '4': 'Боев',
                    '5': 'Процент побед',
                    '6': 'Опыт',
                    '7': 'Урон',
                    '8': 'Потоплено кораблей',
                    '9': 'Урон по засвету',
                    '10': 'Выжил',
                    '11': 'Сбито самолетов',
                    '12': 'Выстрелов',
                    '13': 'Точность',
                    '14': 'Захват',
                    '15': 'Защита',
                    '16': 'Потенциалка',
                    '17': 'Засвечено кораблей',
                    '18': 'Рекорд опыта',
                    '19': 'Рекорд урона',
                    '20': 'Рекорд потопленных кораблей',
                    '21': 'Рекорд сбитых самолётов',
                    '22': 'Рекорд потенциалки',
                    '23': 'Рекорд засвеченных',
                    '24': 'Рекорд урона по засвету',
                    '25': 'Убил/Убит',
                    '26': 'PRO alfa',
                    '27': 'последний бой'}
USER_FILTER_NAMES = ['0', '2', '3', '4', '5', '6', '7', '8', '10', '14', '16', '25', '26', '27']

SHIP_NAME_COLUMN_POSITION = USER_FILTER_NAMES.index('3')

BLOCK_PASS = ['Имя игрока', 'Класс', 'Нация', 'Уровень', 'Корабль']
BLOCK_DIVISION_BY_TWO = ['Процент побед', 'Опыт', 'Урон', 'Потоплено кораблей', 'Урон по засвету', 'Выжил',
                         'Сбито самолетов', 'Выстрелов', 'Точность', 'Захват', 'Защита', 'Потенциалка',
                         'Засвечено кораблей', 'Убил/Убит', 'PRO alfa']
BLOCK_ADDING = ['Боев']
BLOCK_DATA = ['последний бой', 'время']


class TestMainPage:
    clan_page = None
    player_page = None
    great_data = None

    @classmethod
    def setup_class(cls):
        TestMainPage.clan_page = WebClient(URL).load_page()

    def test_table_filter(self, page):
        page.ship_statistic_table.sort_filters(USER_FILTER_NAMES)

    def test_monthly_links(self):
        return self.player_page.last_months_links()

    def test_player_monthly_statistics(self):
        if self.test_monthly_links():
            all_months_data = None
            for page_number in range(len(self.player_page.last_months_links())):
                month_pages = self.player_page.last_months_links()
                inter_page = month_pages[page_number].open()

                self.test_table_filter(inter_page)

                column_names = inter_page.ship_statistic_table.column_names(last_battle=True)
                table_rows = inter_page.ship_statistic_table.table_rows(len(USER_FILTER_NAMES) + 1
                                                                        if '27' in USER_FILTER_NAMES
                                                                        else len(USER_FILTER_NAMES),
                                                                        SHIP_NAME_COLUMN_POSITION)

                if all_months_data is None:
                    all_months_data = pd.DataFrame(table_rows, columns=column_names)
                    all_months_data.insert(0, 'Имя игрока', inter_page.player_name.value)
                else:
                    monthly_data = pd.DataFrame(table_rows, columns=column_names)
                    monthly_data.insert(0, 'Имя игрока', inter_page.player_name.value)

                    all_months_data_ships_list = all_months_data['Корабль'].tolist()
                    for i, monthly_data_row in monthly_data.iterrows():
                        if monthly_data_row['Корабль'] in all_months_data_ships_list:
                            idx = all_months_data[all_months_data['Корабль'] ==
                                                  monthly_data_row['Корабль']].index.to_list()[0]

                            all_months_data_row = all_months_data[all_months_data['Корабль'] == monthly_data_row['Корабль']]

                            for col, val in all_months_data_row.items():
                                if col in BLOCK_DIVISION_BY_TWO:
                                    all_months_data.loc[idx, col] = (val[idx] + monthly_data_row[col]) / 2
                                else:
                                    if col in BLOCK_ADDING:
                                        all_months_data.loc[idx, col] = val[idx] + monthly_data_row[col]
                                    else:
                                        if col in BLOCK_DATA:
                                            all_months_data.loc[idx, col] = monthly_data_row[col]
                        else:
                            all_months_data = all_months_data.append(monthly_data_row, ignore_index=True)
                self.player_page.web_client.driver.back()
            return all_months_data
        else:
            self.player_page.web_client.driver.back()

    def test_get_statistic_all_players(self):
        count_players_links = self.clan_page.players_links()
        for player_link in range(len(count_players_links)):
            self.player_page = self.clan_page.players_links()[player_link].open()
            player_data = self.test_player_monthly_statistics()

            if self.great_data is None:
                self.great_data = player_data
            else:
                self.great_data = pd.concat([self.great_data, player_data], sort=False, axis=0)

            self.player_page.web_client.driver.get(URL)

        writer = pd.ExcelWriter(r'c:\Users\ll\Downloads\rushb_xls.xlsx')
        self.great_data.to_excel(writer)
        writer.save()

    @classmethod
    def setup_teardown(cls):
        cls.clan_page.web_client.driver.quit()


if __name__ == "__main__":
    a = TestMainPage()
    a.setup_class()
    a.test_get_statistic_all_players()
    a.setup_teardown()
