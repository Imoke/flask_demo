from peewee import *

from package.base.database import flask_db, database
from package.models.entities.exampleEntities import *
from .shelfModal import *


class BookModel(ModelSchema):

    shelf = Related()
    potentialShelfs = Related()

    class Meta:
        model = Book

    # more detail about transaction: http://docs.peewee-orm.com/en/latest/peewee/database.html#context-manager
    @classmethod
    @database.atomic()
    def saveBook(cls, name):
        return BookModel(only=("id", "name")).dump(Book.create(name=name))

    @classmethod
    def getAllBooksWithShelf(cls):
        # one to one
        books = Book.select(Book, Shelf).join(Shelf)
        return BookModel(many=True).dumps(books)

    @classmethod
    def getBooksWithPotentialShelf(cls):
        # many to many
        books = Book.select()
        positions = Position.select()
        shelfs = Shelf.select()

        query = prefetch(books, positions, shelfs)
        return BookModel(many=True, only=("id", "name", "potentialShelfs")).dumps(query)
