# Test Task Currency Exchange Rate


## Table of Contents
- [Description](#description)
- [Run Example](#run-example)
- [Arguments](#arguments)
- [Example of Data](#example-of-data)
- [Task Description](#task)


## Description
For launch API, you need to have a start date and a finish date in format DD/MM/YYYY. After it, you are able to choose
which data you need: full data, average data, max data, min data. After receiving data (json), you are able to output 
what you want. I made a few prints as an example: print_average_data, print_min_data_for_every_currency, 
print_max_data_for_every_currency.

[Return](#table-of-contents)


## Run Example
Clone the project

```bash
git clone https://github.com/Danila0987654/test_task_currency_exchange_rate.git
```

Go to the project directory

```bash
cd test_task_currency_exchange_rate
```

Run Example

```bash
python.exe .\example.py date_begin date_end
```

[Return](#table-of-contents)


## Arguments

Dates must be in this format YYYY-MM-DD. You are able to launch only with date_begin then date_end will be -90 days from
your date_begin. 

Also, you are able to launce without arguments then it will take from today -90 days.

[Return](#table-of-contents)


## Example of data

There you are able to see example of the returning data from function get_full_data in class. 

```json
{'R01010': {'CharCode': 'AUD', 'Name': 'Australian Dollar', 'Average': '52.462759', 'Max': {'Date': '15.04.2023', 'Value': 55.2845}, 'Min': {'Date': '15.03.2023', 'Value': 49.9956}}}
```

[Return](#table-of-contents)


## Task

Create a program using API cbr.ru which will:
- Indicate the average value of the ruble exchange rate for the custom period across all currencies
- Indicate the max value of the ruble exchange rate, and this date for the custom period across all currencies
- Indicate the min value of the ruble exchange rate, and this date for the custom period across all currencies

[Return](#table-of-contents)