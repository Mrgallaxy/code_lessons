from tortoise.models import Model
from tortoise import fields, Tortoise

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
