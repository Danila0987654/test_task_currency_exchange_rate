from API.api import API
from functions.functions import receive_dates, print_average_data, print_min_data_for_every_currency

date_begin, date_end = receive_dates()
api_client = API(date_begin, date_end)
full_data = api_client.get_full_data()
# print_average_data(full_data)
print_min_data_for_every_currency(full_data)