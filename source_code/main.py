from get_info import Get_info
from format_data import Format_data
from drawing import Draw_plots
from calculate_statistic import Calculate_statistic

url = open(r"F:\Coding\Projects\data\input_data\plaku_e36.txt", "r").read()
# url = open(r"F:\Coding\Projects\tests\.pytest_cache\test_data\bmw_test.txt", "r").read()

formatter = Format_data()
paint = Draw_plots()
info = Get_info()
calculator = Calculate_statistic()
number_of_sites = info.get_number_of_sites(url)
prices = info.get_prices(url, number_of_sites)
max_value = calculator.count_max(prices)
min_value = calculator.count_min(prices)
amount_of_auctions = len(prices) #nie dziala max to 975?! błąd olx
average_price = calculator.count_average(prices)
prices = formatter.remove_outliers(prices)
date = info.get_date()

print('Average {} zł, Min {} zł, Max {} zł, Date {}, Auctions {}'.format(average_price, min_value, max_value, date,
                                                                         amount_of_auctions))

# #daily point graph
# daily_point_graph(names, sorted(prices))
