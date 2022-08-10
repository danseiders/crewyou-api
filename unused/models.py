# from peewee import *
# from flask_login import UserMixin


# class User(UserMixin, Model):
#     username = CharField(unique=True)
#     email = CharField(unique=True)
#     password = CharField()
#     user_type = CharField()


# class Profiles(Model):
#     user_id = ForeignKeyField(User, backref='profiles')
#     imgURL = CharField()
#     firstName = CharField()
#     lastName = CharField()
#     airport = CharField()
#     about = TextField()
#     position1 = CharField()
#     position2 = CharField()
#     position3 = CharField()
#     position4 = CharField()
#     touring = BooleanField()
#     availability = CharField()
#     # friends = ForeignKeyField(Users, backref='profiles')


# class ManagerProfiles(Model):
#     user_id = ForeignKeyField(User, backref='manager-profiles')
#     business_name = CharField()
#     business_type = CharField()
#     city = CharField()
#     artists = CharField()
