from peewee import *
from db_connection import *
db = PostgresqlDatabase(connect_list()[0].strip(), user=connect_list()[1].strip())


class BaseModel(Model):
    class Meta:
        database = db


class Story(BaseModel):
    title = CharField()
    story = TextField()
    criteria = TextField()
    value = IntegerField()
    estimation = FloatField()
    status = CharField()
