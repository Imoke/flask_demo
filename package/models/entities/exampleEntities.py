from package.base.database import *
from peewee import *


class Shelf(flask_db.Model):
    id = AutoField()
    name = CharField(unique=False)


class Book(flask_db.Model):
    id = AutoField()
    name = CharField(unique=False)
    # book表必须有一个 shelf_id的字段，查询到的shelf自带books数组
    shelf = ForeignKeyField(
        Shelf, backref='books')


class Position(flask_db.Model):
    # position表分别有一个字段叫shelf_id 和 book_id, 连接查询的book类和shelf都会有positions字段
    shelf = ForeignKeyField(Shelf, backref='potentialBooks')
    book = ForeignKeyField(Book, backref='potentialShelfs')
