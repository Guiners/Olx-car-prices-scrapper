# class Get_info(Format_data):
#
#     @staticmethod
#     def get_date():
#         today = date.today()
#         # day = today.strftime("%d/%m/%Y")
#         return today
#
#     @staticmethod
#     def get_prices_and_names(URL):
#         page = get(URL)
#         bs = BeautifulSoup(page.content, features="html.parser")
#         prices = []
#         names = []
#         for offer in bs.find_all('div', class_='offer-wrapper'):
#             name_footer = offer.find('p', class_='price')
#             name = name_footer.find('strong').get_text()
#             if name.find('comp') != -1 or name.find('Comp') != -1 or name.find('Komp') != -1:
#                 pass
#             else:
#                 names.append(name)
#                 price_footer = offer.find('p', class_='price')
#                 prices.append(Format_data.format_price(price_footer.find('strong').get_text()))
#
#         return prices, names
#
#     @staticmethod
#     def get_site_info(url: str, prices: list) -> list:
#         page = get(url)
#         bs = BeautifulSoup(page.content, features="html.parser")
#         for offer in bs.find_all('td', class_='offer'):
#             name_footer = offer.find('p', class_='price')
#             name = name_footer.find('strong').get_text()
#             if name.find('comp') != -1 or name.find('Comp') != -1 or name.find('Komp') != -1:
#                 pass
#             else:
#                 price_footer = offer.find('p', class_='price')
#                 prices.append(Format_data.format_price(price_footer.find('strong').get_text()))
#         return prices
#   ''' for offer in bs.find_all('div', class_='pager rel clr'):
#             numer_footer = offer.find('p', class_='price')
#             number = numer_footer.find('strong').get_text()'''

https://www.olx.pl/motoryzacja/samochody/bmw/seria-3/?search%5Bfilter_float_year%3Afrom%5D=1992&search%5Bfilter_float_year%3Ato%5D=1998&search%5Bfilter_enum_petrol%5D%5B0%5D=petrol&search%5Bfilter_enum_petrol%5D%5B1%5D=lpg&search%5Bfilter_float_enginepower%3Afrom%5D=140&search%5Bfilter_float_enginepower%3Ato%5D=160&search%5Bfilter_enum_car_body%5D%5B0%5D=coupe&search%5Bfilter_enum_transmission%5D%5B0%5D=manual