import sys

from datetime import datetime, timedelta


def receive_dates():
    if len(sys.argv) == 3:
        date_end = datetime.strptime(sys.argv[2], "%Y-%m-%d")
        date_begin = datetime.strptime(sys.argv[1], "%Y-%m-%d")
    elif len(sys.argv) == 2:
        date_end = datetime.strptime(sys.argv[1], "%Y-%m-%d")
        date_begin = datetime.strptime(sys.argv[1], "%Y-%m-%d") - timedelta(days=90)
    else:
        date_end = datetime.now()
        date_begin = datetime.now() - timedelta(days=90)

    return datetime.strftime(date_begin, "%d/%m/%Y"), datetime.strftime(date_end, "%d/%m/%Y")


def print_average_data(input_data):
    for id_code, data in input_data.items():
        print(f"{data['CharCode']}: {data['Average']}")


def print_min_data_for_every_currency(input_data):
    for id_code, data in input_data.items():
        print(f"{data['CharCode']}: Min value {data['Min']['Value']} was in {data['Min']['Date']}")


def print_max_data_for_every_currency(input_data):
    for id_code, data in input_data.items():
        print(f"{data['CharCode']}: Max value {data['Max']['Value']} was in {data['Max']['Date']}")
