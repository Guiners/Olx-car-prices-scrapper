from datetime import date
from bs4 import BeautifulSoup
from requests import get
from format_data import Format_data


class Get_info(Format_data):
    @staticmethod
    def get_date():
        today = date.today()
        # day = today.strftime("%d/%m/%Y")
        return today

    @staticmethod
    def get_site_info(url: str, prices: list) -> [list, list]:
        page = get(url)
        bs = BeautifulSoup(page.content, features="html.parser")
        dupa = bs.find('table', id='offers_table' )
        for offer in dupa.find_all('td', class_='offer'):
            name_footer = offer.find('p', class_='price')
            name = name_footer.find('strong').get_text()
            if name.find('comp') != -1 or name.find('Comp') != -1 or name.find('Komp') != -1:
                pass
            else:
                price_footer = offer.find('p', class_='price')
                prices.append(Format_data.format_price(price_footer.find('strong').get_text()))
        return prices

    @staticmethod
    def get_number_of_sites(url: str) -> int:
        page = get(url)
        bs = BeautifulSoup(page.content, features="html.parser")
        if not bs.find_all('div', class_='pager rel clr'):
            number_of_sites = 1
        else:
            for number_div in bs.find_all('div', class_='pager rel clr'):
                number_of_sites_list = number_div.find('a', class_="block br3 brc8 large tdnone lheight24",
                                                       attrs={"data-cy": "page-link-last"}).get_text()
                number_of_sites = Format_data.format_number(number_of_sites_list)
        return number_of_sites

    def get_prices(self, url: str, number_of_sites: int, prices=[]) -> list:
        prices = self.get_site_info(url, prices)
        if number_of_sites > 1:
            for i in range(2, number_of_sites + 1):
                url1 = url + '&page={}'.format(i)
                prices = self.get_site_info(url1, prices)
        return prices
