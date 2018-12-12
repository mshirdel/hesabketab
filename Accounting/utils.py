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
