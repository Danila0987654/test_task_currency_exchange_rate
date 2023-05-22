from API.api import API
from functions.functions import receive_dates, print_everything

date_begin, date_end = receive_dates()
api_client = API(date_begin, date_end)
full_data = api_client.get_full_data()
print_everything(full_data)
