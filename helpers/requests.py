from uuid import uuid4
from argon2 import PasswordHasher

pass_hash = PasswordHasher()


def get_uuid():
    return str(uuid4())


def get_password_hash(value):
    return pass_hash.hash(value)
