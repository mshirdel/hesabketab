import csv
import jdatetime

from .models import Item, Group


def import_items(user, file_name='data.csv'):
    try:
        with open(file_name, newline='') as csvfile:
            items = csv.reader(csvfile, delimiter=',')
            new_items = []
            for item in items:
                new_items.append(Item(name=item[1],
                                      price=item[2],
                                      date=jdatetime.date(int(item[0].split(
                                          '/')[0]), int(item[0].split('/')[1]), int(item[0].split('/')[2])),
                                      item_type='Exp',
                                      group=Group.objects.get(id=1),
                                      user=user))
            Item.objects.bulk_create(new_items)
    except:
        raise Exception("Error in importing")

def convert_string_date_to_jdate(date):
    import jdatetime
    if date:
        year = int(date.split('-')[0])
        month = int(date.split('-')[1])
        day = int(date.split('-')[2])
        return jdatetime.date(year,month,day)
