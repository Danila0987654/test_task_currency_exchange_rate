import sys

from datetime import datetime, timedelta


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
