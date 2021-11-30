"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime

def print_days():

    delta = datetime.timedelta(days=1)
    now_date = datetime.date.today()
    yesterday = now_date - delta
    month_later = now_date - datetime.timedelta(days=30)

    print(f'вчера: {yesterday}, сегодня: {now_date}, 30 дней назад: {month_later}')


def str_2_datetime(date_string):
    str_2_time = datetime.datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return str_2_time


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
