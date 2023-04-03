from selenium.webdriver.common.by import By


class MainPageLocators:
    PLAYERS_LINKS = (By.XPATH, "//tbody[@aria-live]//a")


class PlayerMainPageLocators:
    LAST_DATE_LINKS = (By.XPATH, "//tbody[@class='main_table_body']/tr/td/a")


class PlayerIntermediatePageLocators:
    GENERAL_TABLE = (By.XPATH, "//table[@class='main_table']")
    SHIP_CLASSES_TABLE = (By.XPATH, "//table[@id='MyClass']")
    SHIP_STATISTIC_TABLE = (By.XPATH, "//table[@id='MyShips']")
    TABLE_FILTERS = (By.XPATH, "//div[@class='columnSelector']/div")
    PLAYER_NAME = (By.XPATH, "//span[@class='nickname']")


class StatisticTableFilter:
    CHECKBOX = (By.XPATH, "./input")
    LABEL = (By.XPATH, "./label")


class TableContent:
    TABLE_HEADER = (By.XPATH, "//table[@id='MyShips']/thead/tr/th")
    TABLE_ROWS = (By.XPATH, "//table[@id='MyShips']/tbody/tr")
