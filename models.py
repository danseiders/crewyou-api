from peewee import *
import datetime
# from flask_login import UserMixin

DATABASE = PostgresqlDatabase('crewyou')

class Users(Model):
    username = CharField()
    email = CharField()
    password = CharField()

    class Meta:
        database = DATABASE

class Profiles(Model):
    # user_id = ForeignKeyField(Users, backref='dogs')
    firstName= CharField()
    lastName= CharField()
    airport= CharField()
    positions= CharField()
    touring= BooleanField()
    
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Users, Profiles], safe=True)
    print('TABLES Created')
    DATABASE.close()