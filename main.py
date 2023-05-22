import sys
import requests

from xml.etree import ElementTree
from datetime import datetime, timedelta


class API:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.url_for_id = f"https://www.cbr.ru/scripts/XML_daily_eng.asp?date_req={self.start_date}"
        self.url_for_currencies = f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={self.start_date}&" \
                                  f"date_req2={self.end_date}&VAL_NM_RQ="
        self.answer = {}
        self.currencies = {}

    def set_id(self):
        response = requests.get(self.url_for_id)
        data = ElementTree.fromstring(response.content)
        for element in data.findall('Valute'):
            id_element = element.get('ID')
            self.answer[id_element] = {}
            self.answer[id_element]["CharCode"] = element.find("CharCode").text
            self.answer[id_element]["Name"] = element.find("Name").text

    def set_currencies(self):
        for id_code in self.answer:
            self.currencies[id_code] = {}
            response = requests.get(self.url_for_currencies + id_code)
            data = ElementTree.fromstring(response.content)
            for record in data.findall("Record"):
                date = record.get("Date")
                value = float(record.find("Value").text.replace(',', '.'))
                currency = record.find("Nominal").text
                rate = value / float(currency)
                self.currencies[id_code][date] = rate

    def set_average_value(self):
        for id_code in self.currencies:
            total_rate = total_count = 0
            for date, value in self.currencies[id_code].items():
                total_rate += value
                total_count += 1
            self.answer[id_code]["Average"] = format(total_rate / total_count, '.6f')

    def set_max_value(self):
        for id_code, data in self.currencies.items():
            max_pair = max(data.items(), key=lambda x: x[1])
            self.answer[id_code]["Max"] = {"Date": max_pair[0], "Value": max_pair[1]}

    def set_min_value(self):
        for id_code, data in self.currencies.items():
            max_pair = min(data.items(), key=lambda x: x[1])
            self.answer[id_code]["Min"] = {"Date": max_pair[0], "Value": max_pair[1]}

    def get_full_data(self):
        self.set_id()
        self.set_currencies()
        self.set_average_value()
        self.set_max_value()
        self.set_min_value()
        return self.answer

    def get_average_data(self):
        self.set_id()
        self.set_currencies()
        self.set_average_value()
        return self.answer

    def print_average_data(self):
        self.set_id()
        self.set_currencies()
        self.set_average_value()
        print(f"Average values for all valute from {self.start_date} to {self.end_date}")
        for id_code, data in self.answer.items():
            print(f"{data['CharCode']}: {data['Average']}")


def receive_dates():
    if len(sys.argv) == 3:
        date_end = datetime.strptime(sys.argv[1], "%Y-%m-%d")
        date_begin = datetime.strptime(sys.argv[2], "%Y-%m-%d")
    elif len(sys.argv) == 2:
        date_end = datetime.strptime(sys.argv[1], "%Y-%m-%d")
        date_begin = datetime.strptime(sys.argv[1], "%Y-%m-%d") - timedelta(days=90)
    else:
        date_end = datetime.now()
        date_begin = datetime.now() - timedelta(days=90)

    return datetime.strftime(date_begin, "%d/%m/%Y"), datetime.strftime(date_end, "%d/%m/%Y")


date_begin, date_end = receive_dates()
api_client = API(date_begin, date_end)
# full_data = api_client.get_full_data()
# average = api_client.get_average_data()
api_client.print_average_data()

