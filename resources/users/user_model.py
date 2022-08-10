from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, BooleanAttribute
from flask_login import UserMixin


class UserModel(UserMixin, Model):
    class Meta:
        table_name = 'users'

    username = UnicodeAttribute()
    email = UnicodeAttribute()
    password = UnicodeAttribute()
    user_type = UnicodeAttribute()
    is_active = BooleanAttribute()
