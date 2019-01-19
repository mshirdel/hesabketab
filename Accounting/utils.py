import csv
import jdatetime

from .models import Item, Group


def import_items(user, file_name='data.csv'):
    # try:
    with open(file_name, newline='') as csvfile:
        items = csv.reader(csvfile, delimiter=',')
        new_items = []
        for item in items:
            new_items.append(Item(name=item[1],
                                    price=item[2],
                                    date=jdatetime.date(int(item[0].split(
                                        '/')[0]), int(item[0].split('/')[1]), int(item[0].split('/')[2])),
                                    item_type='Exp',
                                    group=Group.objects.filter(user=user).first(),
                                    user=user))
        Item.objects.bulk_create(new_items)
        return len(new_items)
    # except:
    #     raise Exception("خطا در بارگزاری فایل csv")


def convert_string_date_to_jdate(date):
    if date:
        year = int(date.split('-')[0])
        month = int(date.split('-')[1])
        day = int(date.split('-')[2])
        return jdatetime.date(year, month, day)


def get_last_12_month_period(jdate):
    result = []
    number_of_days_in_one_year = 365
    if jdate.isleap():
        number_of_days_in_one_year = 366
    one_year_ago = jdate - jdatetime.timedelta(number_of_days_in_one_year)
    # result.append(get_month_period(one_year_ago))
    one_year_ago = one_year_ago + \
        jdatetime.timedelta(get_jmonth_days(one_year_ago))
    while one_year_ago < jdate + jdatetime.timedelta(30):
        result.append(get_month_period(one_year_ago))
        one_year_ago = one_year_ago + \
            jdatetime.timedelta(get_jmonth_days(one_year_ago))
    return result


def get_month_period(jdate):
    end_of_month = 30
    if jdate.month < 7:
        end_of_month = 31
    elif jdate.month == 12 and not jdate.isleap():
        end_of_month = 29
    return (jdatetime.date(jdate.year, jdate.month, 1), jdatetime.date(jdate.year, jdate.month, end_of_month))


def get_jmonth_days(jdate):
    end_day = 30
    if jdate.month < 7:
        end_day = 31
    elif jdate.month == 12 and jdate.isleap():
        end_day = 29
    return end_day
