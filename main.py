import csv
from peewee import *

db = PostgresqlDatabase(database='test', user='postgres', password='1234', host='localhost')


class Radiator(Model):
    name = CharField()
    price = CharField()
    stock = TextField()
    url = TextField()

    class Meta:
        database = db


def main():
    db.connect()
    db.create_tables([Radiator])

    with open('catalog_kontur.csv') as file:
        order = ['name', 'price', 'stock', 'url']
        reader = csv.DictReader(file, fieldnames=order)
        radiators = list(reader)

        for row in radiators:
            radiator = Radiator(name=row['name'], price=row['price'],
                                stock=row['stock'], url=row['url'])
            radiator.save()



if __name__ == '__main__':
    main()
