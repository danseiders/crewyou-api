from peewee import *
import datetime
# from flask_login import UserMixin

DATABASE = PostgresqlDatabase('crewyou')

class Dog(Model):
    username = CharField()
    email = CharField()
    password = CharField()

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Dog], safe=True)
    print('TABLES Created')
    DATABASE.close()