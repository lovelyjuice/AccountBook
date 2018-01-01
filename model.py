from peewee import *

db = SqliteDatabase('database.db', pragmas=(('foreign_keys', 'on'),))


class Users(Model):
    id = SmallIntegerField(primary_key=True)
    name = CharField(unique=True)
    info = TextField(null=False)

    class Meta:
        database = db


class Types(Model):
    type = CharField(unique=True)

    class Meta:
        database = db


class Charges(Model):
    id = SmallIntegerField(primary_key=True)
    type = ForeignKeyField(Types, to_field='type')
    amount = FloatField()
    date = DateField(default='date(\'now\')')
    username = ForeignKeyField(Users, to_field='name')
    info = TextField()

    class Meta:
        database = db
