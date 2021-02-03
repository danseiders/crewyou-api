import os
from peewee import *
import datetime
from flask_login import UserMixin
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('DATABASE_URL'))
else:
    DATABASE = PostgresqlDatabase('crewyou')
class Users(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    crew = BooleanField()

    class Meta:
        database = DATABASE

class Profiles(Model):
    user_id = ForeignKeyField(Users, backref='profiles')
    imgURL= CharField()
    firstName= CharField()
    lastName= CharField()
    airport= CharField()
    about= TextField()
    position1= CharField()
    position2= CharField()
    position3= CharField()
    position4= CharField()
    touring= BooleanField()
    availability= CharField()
    # friends = ForeignKeyField(Users, backref='profiles')
    
    
    class Meta:
        database = DATABASE

class ManagerProfiles(Model):
    user_id = ForeignKeyField(Users, backref='manager-profiles')
    company = CharField()
    city = CharField()
    artists = CharField()

    class Meta: 
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Users, Profiles, ManagerProfiles], safe=True)
    print('TABLES Created')
    DATABASE.close()